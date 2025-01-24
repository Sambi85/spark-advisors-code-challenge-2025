# README - Spark Advisors Code Challlenge 2025

  **Summary:**
  - My solution is a python script at it's core
  - The script seperates concerns into 3 main areas - Scripting Setup, Helper functions, and CSV generation based on provided files
  - Please note a new CSV file will be generated with previous data to preserve data integrity
  - An additonal logging file has been added for easier debugging
  - A basic test suite has been added to maintain the provided helper functions

# Running the Python Script
  - Navigate to the root directory of the project
  - In terminal:
```bash
  python3 solution.py
```

  - For an updated csv file go here => ./data/updated_slcsp_<TIMESTAMP>.csv
  - For a detailed logging output go here => ./logs/*

# Running the Test Suite
  - Navigate to the root directory of the project
  - In terminal: For helpers.py
```bash
  python3 -m unittest test_helpers.py
```

  - Please note, it's expected to raise logging in terminal when running the test suite

# Notes on my Approach:
  - Determine the 2nd lowest cost (silver plan) for a group of zipcodes

  **Provided Files:**
  - `slcsp.csv` — Update this file, second column with the rate (see below) of the corresponding SLCSP
  - `plans.csv` — all the health plans in the U.S. on the marketplace
  - `zips.csv` — a mapping of ZIP code to county/counties & rate area(s)
  - `README.md` — outlines the challenge

  **Input:**
  - `CSV file 1` => slcsp.csv (will update this)
  - `CSV file 2` => plans.csv
  - `CSV file 3` => zips.csv

  **Output:** 
  - Updated CSV file => `slcsp.csv`
  - Emit the answer on `stdout (terminal output)`
  - Emitted values should be in the `same CSV format` as the input => `zipcode`, `rate`
  - Positioning of the **columns** and **rows** should be the same as the original csv file
  - Float values should be formatted to **2 decimal places** =>**245.20**
  - Missing values should be left blank

  **What the happy path looks like:**
  - Use zipcode to look up the rate area
  - Use rate area and metal level(silver) to gather all plans
  - Grab the 2nd lowest cost plan
  - Update the slcsp.csv file with the 2nd lowest cost plan under rate column

  **Identified Edge Cases:**
  1. It's possible that there can be no 2nd lowest cost plan, leave the rate column blank
  2. A zipcode can potentially be in multiple counties.
    - If the county cannot be determined, it may still be possible to determine the rate area for zipcode.
    - We need to check if the county column contains multiple counties

  3. A zipcode can also be in more than one rate area. 
    - In that case, the answer is ambiguous and should be left blank.