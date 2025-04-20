import pandas as pd

def summarize_categorical_distributions(df: pd.DataFrame, min_category_threshold=0.05):
    df_clean = df.dropna()

    categorical = df_clean.select_dtypes(include=['object', 'category']).columns
    summary = {}

    for col in categorical:
        value_counts = df_clean[col].value_counts(normalize=True)
        dist = value_counts.to_dict()

        # Detect categories with less than threshold %
        underrepresented = [k for k, v in dist.items() if v < min_category_threshold]

        summary[col] = {
            "distribution": dist,
            "underrepresented": underrepresented,
            "max_ratio": max(dist.values()) if dist else None
        }

    return summary