# Helper functions for solution.py
# The main purpose of this is file is to seprate of concerns
import csv
import os
import logging

# Grab the unique rate area we need, based on a given zipcode
def get_rate_area(zipcode,  zips_path):
    rate_areas = set()
    with open(zips_path, mode='r', newline='', encoding='utf-8') as zips_file:
        csv_reader = csv.DictReader(zips_file)
        for row in csv_reader:
            if row['zipcode'] == zipcode:
                rate_areas.add(row['rate_area'])

    if len(rate_areas) > 1:
        logging.warning(f"Invalid Rate - Multiple rate areas found for ZIP {zipcode}: {', '.join(rate_areas)} !!!")
        return None
    elif len(rate_areas) == 1:
        return rate_areas.pop()
    
    logging.warning(f"Invalid rate - No rate area found for ZIP {zipcode} !!!")
    return None


# Grab the silver plans we need for a given rate area...
def get_second_lowest_silver_plan(rate_area, plans_path):
    silver_plans = []
    with open(plans_path, mode='r', newline='', encoding='utf-8') as plans_file:
        csv_reader = csv.DictReader(plans_file)
        for row in csv_reader:
            if row['metal_level'] == 'Silver' and row['rate_area'] == rate_area:
                silver_plans.append(float(row['rate']))
    
    # Sort silver plans, find the 2nd lowest cost, if not enough plans don't return anything...
    silver_plans = sorted(silver_plans)
    if len(silver_plans) >= 2:
        logging.warning(f"Target Silver Plan Not found, need at least 2 plans for rate_area: {rate_area} !!!")
        return silver_plans[1]
    return None
