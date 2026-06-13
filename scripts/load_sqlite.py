import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mutual_fund.db")

tables = {
    "fund_master": "data/processed/01_fund_master.csv",
    "nav_history": "data/processed/nav_history_clean.csv",
    "scheme_performance": "data/processed/scheme_performance_clean.csv",
    "investor_transactions": "data/processed/investor_transactions_clean.csv"
}

for table, path in tables.items():
    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(table, len(df))