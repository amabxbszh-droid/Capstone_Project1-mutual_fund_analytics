import pandas as pd

df = pd.read_csv(
    "data/processed/08_investor_transactions.csv"
)

# Fix date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Validate amount
df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]

invalid_txns = df[
    ~df["transaction_type"].isin(valid_types)
]

print("Invalid Transaction Types:")
print(invalid_txns["transaction_type"].unique())

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nRows:", len(df))