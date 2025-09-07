import os

def save_file(df, original_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True) 
    file = clean_name(original_path)
    out_path = os.path.join(output_dir, file)   

    if original_path.endswith('.csv'):
        df.to_csv(out_path, index=False)
    elif original_path.endswith('.xlsx'):
        df.to_excel(out_path, index=False)

# append datafile name with _clean
def clean_name(filepath):
    file = os.path.basename(filepath)
    file = os.path.splitext(file)
    clean_name = file[0]+"_clean"+file[1]
    return clean_name
