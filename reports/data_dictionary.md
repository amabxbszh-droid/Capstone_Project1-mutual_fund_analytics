# Data Dictionary

## 01_fund_master.csv

| Column        | Data Type | Business Definition               |
| ------------- | --------- | --------------------------------- |
| amfi_code     | Integer   | Unique AMFI scheme identifier     |
| scheme_name   | String    | Mutual fund scheme name           |
| fund_house    | String    | Asset Management Company (AMC)    |
| category      | String    | Broad fund category (Equity/Debt) |
| sub_category  | String    | Detailed scheme classification    |
| risk_category | String    | Investor risk level               |

Source: Fund Master Dataset

---

## 02_nav_history.csv

| Column    | Data Type | Business Definition      |
| --------- | --------- | ------------------------ |
| amfi_code | Integer   | Scheme identifier        |
| date      | Date      | NAV observation date     |
| nav       | Float     | Net Asset Value per unit |

Source: Historical NAV Dataset

---

## 07_scheme_performance.csv

| Column             | Data Type | Business Definition               |
| ------------------ | --------- | --------------------------------- |
| amfi_code          | Integer   | Scheme identifier                 |
| scheme_name        | String    | Fund name                         |
| return_1yr_pct     | Float     | 1-year return (%)                 |
| return_3yr_pct     | Float     | 3-year return (%)                 |
| return_5yr_pct     | Float     | 5-year return (%)                 |
| benchmark_3yr_pct  | Float     | Benchmark return (%)              |
| alpha              | Float     | Alpha measure                     |
| beta               | Float     | Beta measure                      |
| sharpe_ratio       | Float     | Risk-adjusted return metric       |
| sortino_ratio      | Float     | Downside-risk-adjusted return     |
| std_dev_ann_pct    | Float     | Annualized volatility             |
| max_drawdown_pct   | Float     | Maximum drawdown (%)              |
| aum_crore          | Float     | Assets under management (₹ crore) |
| expense_ratio_pct  | Float     | Expense ratio (%)                 |
| morningstar_rating | Integer   | Fund rating                       |
| risk_grade         | String    | Risk classification               |

Source: Scheme Performance Dataset

---

## 08_investor_transactions.csv

| Column             | Data Type | Business Definition        |
| ------------------ | --------- | -------------------------- |
| investor_id        | Integer   | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Scheme identifier          |
| transaction_type   | String    | SIP / Lumpsum / Redemption |
| amount_inr         | Float     | Transaction amount in INR  |
| state              | String    | Investor state             |
| city               | String    | Investor city              |
| city_tier          | String    | Tier classification        |
| age_group          | String    | Investor age segment       |
| gender             | String    | Investor gender            |
| annual_income_lakh | Float     | Annual income in lakhs     |
| payment_mode       | String    | Payment channel            |
| kyc_status         | String    | KYC verification status    |

Source: Investor Transactions Dataset

---

## Data Quality Notes

* Blank rows removed during cleaning.
* Duplicate records removed.
* NAV values validated to be greater than zero.
* Transaction amounts validated to be positive.
* Transaction types standardized.
* Date fields converted to datetime format.
* AMFI codes validated against NAV history.
