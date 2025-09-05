def generate_summary(df_before, df_after, n_dates):
    summary = {
        "duplicates_removed": get_n_duplicates(df_before, df_after),
        "missing": get_n_nan(df_before),
        "dates_fixed": int(n_dates)
    }
    return summary

def get_n_duplicates(df_before, df_after):
    n = df_before.count() - df_after.count()
    return int(n.sum())

def get_n_nan(df):
    count = df.isnull().sum().sum()
    return int(count)
    
