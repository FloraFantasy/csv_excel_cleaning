import pandas as pd
# returns df
# decideds if its csv or xlsx file

def load_file(filepath):
    print(filepath)
    if filepath.endswith('.csv'):
        return load_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return load_xlsx(filepath)
    raise ValueError("Unknown file extension")

def load_csv(file):
    print(f"{file} is csv file")
    df = pd.read_csv(file)
    return df

def load_xlsx(file):
    print(f"{file} is excel file")
    df = pd.read_excel(file)
    return df