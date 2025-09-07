from cleaner import file_loader, cleaning, file_saver, summary

def run_pipeline(file_path, output_dir="outputs/", fill_strategy="N/A"):
    # Load file
    df = file_loader.load_file(file_path)

    # Cleaning steps
    clean_df, dates_converted = cleaning.fix_dates(df)
    clean_df = cleaning.trim_spaces(clean_df)
    clean_df = cleaning.normalize_text(clean_df)
    clean_df = cleaning.remove_duplicates(clean_df)
    clean_df = cleaning.fill_missing(clean_df, fill_strategy)

    # Save cleaned file
    file_saver.save_file(clean_df, file_path, output_dir)

    # Generate summary
    report = summary.generate_summary(df, clean_df, dates_converted)

    return clean_df, report

# This keeps it runnable directly too
if __name__ == "__main__":
    run_pipeline("data/messy_data.csv")
