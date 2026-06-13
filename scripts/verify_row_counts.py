from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///mutual_fund.db"
)

tables = [
    "fund_master",
    "nav_history",
    "scheme_performance",
    "investor_transactions"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as count FROM {table}",
        engine
    )

    print("\nTable:", table)
    print(count)