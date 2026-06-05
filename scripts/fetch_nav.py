import requests
import pandas as pd

codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/nav_{code}.csv",
        index=False
    )

    print(code, "saved")