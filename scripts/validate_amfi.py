import pandas as pd

fund_master = pd.read_csv(
    "data/processed/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/processed/02_nav_history.csv"
)

master_codes = set(
    fund_master["amfi_code"].dropna()
)

nav_codes = set(
    nav_history["amfi_code"].dropna()
)

missing = master_codes - nav_codes

print("Fund Master Codes:", len(master_codes))
print("NAV Codes:", len(nav_codes))
print("Missing Codes:", len(missing))
print(missing)