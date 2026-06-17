import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

funds = perf[
    perf["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

top3 = funds.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(
    top3[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio"
        ]
    ]
)