import pandas as pd

def load_reviews(path: str, limit: int = 10000) -> pd.DataFrame:
    if path.endswith('.xlsx'):
        df = pd.read_excel(path)
    else:
        raise ValueError("Unsupported file type")
    # Map your actual columns to the expected names
    rename_map = {
        'review_text': 'reviewText',
        'review_title': 'summary',
        'customer_review_rating': 'overall'
    }
    df = df.rename(columns=rename_map)
    cols = ['reviewText', 'summary', 'overall']
    df = df[cols].dropna()
    return df.sample(n=min(limit, len(df)), random_state=42)