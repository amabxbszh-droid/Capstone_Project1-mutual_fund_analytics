import pandas as pd

df = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

    anomalies = df[
        (df[col] < -100) |
        (df[col] > 200)
    ]

    print(f"{col} anomalies:",
          len(anomalies))

df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

expense_flags = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense ratio anomalies:",
    len(expense_flags)
)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Rows:", len(df))