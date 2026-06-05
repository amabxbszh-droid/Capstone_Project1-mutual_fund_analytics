import pandas as pd
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

for file in os.listdir(RAW_DIR):

    if file.endswith(".csv"):

        path = os.path.join(RAW_DIR, file)

        df = pd.read_csv(path)

        # Remove unnamed columns
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        # Remove fully empty rows
        df = df.dropna(how="all")

        # Remove duplicates
        df = df.drop_duplicates()

        output = os.path.join(PROCESSED_DIR, file)

        df.to_csv(output, index=False)

        print(f"{file} cleaned")
        print("Rows:", len(df))