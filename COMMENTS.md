# Spark Advisors Code Challlenge 2025

Summary:
- My solution is a python script at it's core
- There are 3 main sections - Setup, helper functions, and updating the provided csv
- Added additonal logging for easier debugging 

# Running the Python Script
- Navigate to the root directory of the project
- In terminal:
  python3 solution.py

- For an upated csv file go here => ./data/updated_slcsp.csv
- For detailed logging output go here => ./logs/log.txt
- Please note log.txt is setup to be overwritten on each run by default

# Running the Test Suite
- Navigate to the root directory of the project
- In terminal: For helpers.py
  python3 -m unittest test_helpers.py

- Please note, it's expected to raise logging in terminal when running the test suite

# Notes on my Approach:
- Determine the 2nd lowest cost (silver plan) for a group of zipcodes

Provided Files:
`slcsp.csv` — Update this file, second column with the rate (see below) of the corresponding SLCSP
`plans.csv` — all the health plans in the U.S. on the marketplace
`zips.csv` — a mapping of ZIP code to county/counties & rate area(s)
`README.md` — outlines the challenge

Input:
- CSV file => slcsp.csv, update this
- CSV file => plans.csv
- CSV file => zips.csv

Output: 
- Updated CSV file => slcsp.csv
- Emit the answer on stdout (log output)
- Emitted values should be in the same CSV format as the input => zipcode, rate
- float values should be formatted to 2 decimal places => 245.20
- missing values should be left blank

What the happy path looks like:
- Use zipcode to look up the rate area
- Use rate area and metal level(silver) to gather all plans
- Grab the 2nd lowest cost plan
- Update the slcsp.csv file with the 2nd lowest cost plan under rate column

Identified Edge Cases:
- If there is no 2nd lowest cost plan, leave the rate column blank
- If a ZIP code maps to multiple rate areas in the zips.csv file, we will return None or leave the rate blank because we can't definitively determine the second-lowest cost.

# References
- n/a