import csv
import os
import logging

# Script Setup ---------------------------------------------------------------------------------------------

plans = './data/plans.csv'
slscp = './data/slcsp.csv'
zipcodes = './data/zips.csv'

# Dynamicially handle the file paths (future proofing/maintaibility)
data_folder = os.path.join(os.getcwd(), './data')

# Provided CSV file paths
target_path = os.path.join(data_folder, 'slcsp.csv')
plans_path = os.path.join(data_folder, 'plans.csv')
zips_path = os.path.join(data_folder, 'zips.csv')

# Path to the output file (preserving the original file for data integrity/fault tolerance)
updated_sclsp_path = os.path.join(data_folder, 'updated_slcsp.csv')

# Path to the log file, let's save a copy of log for future reference
log_file_path = os.path.join(os.getcwd(), 'logs', 'log.txt')

# Setup logger
logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# logging counter for updates
update_count = 0  

# Helper functions ----------------------------------------------------------------------------

# Fetch the zipcodes we need...
def get_rate_area(zipcode):
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
def get_second_lowest_silver_plan(rate_area):
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

# Updating CSV file + Logging -----------------------------------------------------------------------------------
with open(target_path, mode='r', newline='', encoding='utf-8') as slcsp_file, \
     open(updated_sclsp_path, mode='w', newline='', encoding='utf-8') as updated_file, \
     open(log_file_path, mode='w', encoding='utf-8') as log_file:
    
    csv_reader = csv.DictReader(slcsp_file)
    fieldnames = csv_reader.fieldnames
    csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()

    print(','.join(fieldnames)) # Dynamically print the headers...

    for row in csv_reader:
        zipcode = row['zipcode']
        rate_area = get_rate_area(zipcode) # Use helper function here...
        
        if rate_area:
            logging.info(f"Found rate area {rate_area} for ZIP {zipcode}")
            second_lowest_rate = get_second_lowest_silver_plan(rate_area) # Use helper function here...
            
            if second_lowest_rate is not None:
                row['rate'] = f"{second_lowest_rate:.2f}"
                update_count += 1 
                logging.info(f"Updated: ZIP {zipcode} - Rate Area {rate_area} - SLCSP {second_lowest_rate:.2f}")
                print(f"{zipcode},{second_lowest_rate:.2f}")
            else:
                # Edgecase: Handle second-lowest plan not found, leave this blank...
                row['rate'] = ''
                logging.warning(f"No second-lowest plan for ZIP {zipcode} - Rate Area {rate_area} !!!")
                print(f"{zipcode},")
        else:
            # Edgecase: Handle rate area not found, leave rate blank...
            row['rate'] = ''
            logging.warning(f"No definitive rate area for ZIP {zipcode}. Rate left blank !!!")
            print(f"{zipcode},")
        
        csv_writer.writerow(row)

logging.info(f"Processing complete. Total number of updates made: {update_count}")

print(f"Processing complete. Updated file written to 'updated_slcsp.csv' and log written to 'log.txt'.")
