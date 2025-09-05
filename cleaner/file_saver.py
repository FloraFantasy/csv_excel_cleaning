import pandas as pd
import os

def load_file(df, orginal_path, output_dir='outputs/'):
    file = clean_name(df, orginal_path)
    if orginal_path.endswith('.csv'):
        df.to_csv(output_dir+file)
        return
    elif orginal_path.endswith('.xlsx'):
        df.to_excel(output_dir+file)
        return
    

def clean_name(df, filepath):
    file = os.path.basename(filepath)
    file = os.path.splitext(file)
    clean_name = file[0]+"_clean"+file[1]
    return clean_name
