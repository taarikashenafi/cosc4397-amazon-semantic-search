import argparse
from data.load_data import load_reviews
from src.retrieval.boolean import boolean_search
import csv
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Run Boolean baseline search on Amazon reviews.")
    parser.add_argument('--data', type=str, default='data/raw/reviews_segment.xlsx', help='Path to Excel file')
    parser.add_argument('--limit', type=int, default=5000, help='Number of reviews to load')
    parser.add_argument('--query', type=str, required=True, help='Query string (e.g., "audio quality poor")')
    parser.add_argument('--top', type=int, default=10, help='Number of top results to show')
    args = parser.parse_args()

    df = load_reviews(args.data, limit=args.limit)
    results = boolean_search(df, args.query)
    print(f"\nFound {len(results)} matching reviews for query: '{args.query}'\n")
    for idx, row in enumerate(results[:args.top]):
        print(f"[{idx}] SUMMARY: {row['summary']}\nREVIEW: {row['reviewText']}\n")

    # Mark relevant results
    relevant = input(f"\nEnter comma-separated indices of relevant reviews from 0 to {min(args.top, len(results))-1}: ")
    relevant_indices = set()
    if relevant.strip():
        relevant_indices = set(int(i) for i in relevant.split(',') if i.strip().isdigit())
    precision = len(relevant_indices) / min(args.top, len(results)) if results else 0.0
    print(f"\nPrecision@{args.top}: {precision:.2f}")

    # Save judgment log
    log_row = {
        'timestamp': datetime.now().isoformat(),
        'query': args.query,
        'relevant_indices': ','.join(str(i) for i in sorted(relevant_indices)),
        'top_k': args.top,
        'precision': precision
    }
    log_file = 'judgment_log.csv'
    write_header = False
    try:
        with open(log_file, 'r') as f:
            pass
    except FileNotFoundError:
        write_header = True
    with open(log_file, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=log_row.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(log_row)
    print(f"Judgment log saved to {log_file}")

if __name__ == "__main__":
    main() 