-- Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV per month
SELECT
month,
AVG(nav)
FROM fact_nav fn
JOIN dim_date dd
ON fn.date_key=dd.date_key
GROUP BY month;

-- SIP YoY Growth
SELECT
year,
SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- Transactions by State
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Top 5 performing funds
SELECT *
FROM fact_performance
ORDER BY return_5y DESC
LIMIT 5;

-- Average NAV by fund
SELECT fund_key, AVG(nav)
FROM fact_nav
GROUP BY fund_key;

-- Redemption totals
SELECT SUM(amount)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- Fund count by category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- Risk category distribution
SELECT risk_category, COUNT(*)
FROM dim_fund
GROUP BY risk_category;