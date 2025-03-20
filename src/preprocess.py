import pandas as pd
import os

def load_dataset(file_path):
    """Loads the CTU-13 dataset CSV file into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path, low_memory=False)
    print(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns.")
    
    return df

def preprocess_data(df):
    """Extracts necessary columns and filters TCP traffic."""
    df = df[['SrcAddr', 'DstAddr', 'Proto', 'State']].copy()
    df = df[df['Proto'].str.lower() == 'tcp']
    return df
