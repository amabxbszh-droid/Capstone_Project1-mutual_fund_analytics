# Day 1 Data Quality Report

## Overview

Ten mutual fund datasets were ingested, profiled, cleaned, and validated.

## Key Findings

* Initial datasets contained numerous blank rows generated during spreadsheet export.
* Multiple unused columns named "Unnamed:*" were present.
* Duplicate records were largely caused by trailing empty rows.
* After cleaning, datasets were reduced to valid records only.

## Data Cleaning Performed

1. Removed fully blank rows.
2. Dropped all Unnamed columns.
3. Removed duplicate records.
4. Preserved all valid observations.

## AMFI Code Validation

Fund Master AMFI Codes: 40

NAV History AMFI Codes: 40

Missing Codes: 0

All AMFI scheme codes present in Fund Master were successfully matched with NAV History records.

## Dataset Coverage

* 40 mutual fund schemes
* 46,000 NAV observations
* 32,778 investor transactions
* 8,050 benchmark index observations
* 322 portfolio holding records

## Conclusion

The datasets passed initial validation checks and are suitable for exploratory analysis, performance analytics, portfolio studies, investor behavior analysis, and dashboard development.
