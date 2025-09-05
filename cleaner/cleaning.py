import pandas as pd

def fix_dates(df):
    for col in df.columns:
        if "Date" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce", infer_datetime_format=True, format="mixed")
            fixed = df[col].count()
    return df, fixed
#df[col] = pd.to_datetime(df[col], format="mixed")

def fill_missing(df, strategy):
    # By default everything "N/A"
    fill_values = {col: strategy for col in df.columns}
    # Except Amount → 0
    for col in df.columns:
        if df[col].dtype != object:
            fill_values[col] = 0
    return df.fillna(fill_values)

def trim_spaces(df):
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.strip()
    return df

def normalize_text(df):
    for col in df.columns:
        if df[col].dtype == object and "Email" not in col:
            df[col] = df[col].str.capitalize()
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df