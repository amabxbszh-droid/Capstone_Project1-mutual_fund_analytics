import pandas as pd
import os

RAW_DIR = "data/raw"

files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]

for file in files:
    print("\n" + "=" * 80)
    print("FILE:", file)

    try:
        df = pd.read_csv(os.path.join(RAW_DIR, file))

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print("ERROR:", e)