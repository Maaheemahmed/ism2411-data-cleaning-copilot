mkdir -p src
cat > src/data_cleaning.py <<'PY'
"""
Data cleaning pipeline for sales_data_raw.csv
"""

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV at file_path into a pandas DataFrame."""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = load_data("data/raw/sales_data_raw.csv")
    print("Loaded rows:", len(df))
    print(df.head())
PY