from cleaner import file_loader, cleaning, file_saver, summary

# first calles load_file(filepath)
file_path = "data/messy_data.csv"
df = file_loader.load_file(file_path)
print("Before cleaning:\n", df)
print(df.info())

# calls cleaning functions
clean_df, dates_converted = cleaning.fix_dates(df)
clean_df = cleaning.trim_spaces(clean_df)
clean_df = cleaning.normalize_text(clean_df)
clean_df = cleaning.remove_duplicates(clean_df)
clean_df = cleaning.fill_missing(clean_df, "N/A")
print("\nAfter cleaning:\n", clean_df.to_string())

# safe file
file_saver.load_file(clean_df, file_path)

# create summary
summary = summary.generate_summary(df, clean_df, dates_converted)
print(summary)