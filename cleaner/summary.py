def generate_summary(df_before, df_after):
    n_duplicates = get_n_duplicates(df_before, df_after)
    return n_duplicates[1]

def get_n_duplicates(df_before, df_after):
    n = df_before.count() - df_after.count()
    return n

def get_n_filled():
    ...

"""
{
    "duplicates_removed": X,
    "missing_filled": Y,
    "dates_fixed": Z
}
"""