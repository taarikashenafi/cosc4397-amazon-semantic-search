import re

def simple_tokenize(text):
    return re.findall(r'\w+', text.lower())

def boolean_search(df, query: str):
    query_tokens = set(simple_tokenize(query))
    results = []

    for _, row in df.iterrows():
        tokens = set(simple_tokenize(row['reviewText'] + ' ' + row['summary']))
        if query_tokens.issubset(tokens):
            results.append(row)

    return results