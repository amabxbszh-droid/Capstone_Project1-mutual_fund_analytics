import pandas as pd

df = pd.read_csv("data/processed/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

df = df.sort_values(["amfi_code", "date"])

df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df[df["nav"] > 0]

df = df.drop_duplicates()

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Rows:", len(df))
print("Null NAV:", df["nav"].isna().sum())