# Day 2: Data Cleaning and SQLite Database Report

## Objective

The objective of Day 2 was to clean the processed datasets, validate data quality, design a relational database schema, load the data into SQLite, and prepare analytical SQL queries.

## Data Cleaning Activities

### NAV History

Actions performed:

* Converted date column to datetime format.
* Sorted records by AMFI code and date.
* Forward-filled missing NAV values.
* Removed duplicate records.
* Validated that all NAV values were greater than zero.

Results:

* Total records: 46,000
* Null NAV values after cleaning: 0

### Investor Transactions

Actions performed:

* Converted transaction dates to datetime format.
* Standardized transaction types.
* Validated transaction amounts.
* Reviewed KYC status values.

Results:

* Transaction types validated successfully.
* KYC statuses identified:

  * Verified
  * Pending
* Total records: 32,778

### Scheme Performance

Actions performed:

* Converted return fields to numeric values.
* Checked for abnormal return values.
* Validated expense ratio ranges.
* Flagged any anomalies for review.

Results:

* Dataset cleaned and saved for database loading.
* Total records: 40

## AMFI Validation

Validation was performed between Fund Master and NAV History datasets.

Results:

* Fund Master Codes: 40
* NAV History Codes: 40
* Missing Codes: 0

Conclusion:

All mutual fund schemes in the master dataset have corresponding NAV history records.

## SQLite Database Design

A star-schema style design was prepared.

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

Primary and foreign key relationships were defined to support analytical queries.

## Database Loading Results

| Table                 | Records |
| --------------------- | ------: |
| fund_master           |      40 |
| nav_history           |  46,000 |
| scheme_performance    |      40 |
| investor_transactions |  32,778 |

Verification confirmed that SQLite row counts matched source datasets.

## Analytical SQL Queries Prepared

The following analytical queries were developed:

1. Top 5 funds by AUM
2. Average NAV by month
3. SIP year-over-year growth
4. Transactions by state
5. Funds with expense ratio below 1%
6. Top-performing funds
7. Average NAV by fund
8. Redemption analysis
9. Fund count by category
10. Risk category distribution

## Deliverables Completed

* Data cleaning scripts
* SQLite schema design
* SQLite database creation
* Data loading pipeline
* Validation checks
* Analytical SQL queries
* Data dictionary documentation

## Conclusion

Day 2 successfully established a clean and validated analytical database environment. All datasets were loaded into SQLite, row counts were verified, and analytical SQL queries were prepared for subsequent reporting and dashboard development.
