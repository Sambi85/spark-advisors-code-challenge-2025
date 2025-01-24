import csv
import os
import logging
from helpers import get_rate_area, get_second_lowest_silver_plan # importing custom helper functions

plans = './data/plans.csv'
slscp = './data/slcsp.csv'
zipcodes = './data/zips.csv'

data_folder = os.path.join(os.getcwd(), './data') # dynamicially handle the file paths (future proofing/maintaibility)

target_path = os.path.join(data_folder, 'slcsp.csv')
plans_path = os.path.join(data_folder, 'plans.csv')
zips_path = os.path.join(data_folder, 'zips.csv')

updated_sclsp_path = os.path.join(data_folder, 'updated_slcsp.csv') # write path (used for data integrity/fault tolerance/reliability)
log_file_path = os.path.join(os.getcwd(), 'logs', 'log.txt') # write path for log file (more context for debugging/maintaibility)

# Setup logger
logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

update_count = 0 # logging counter for updates


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
        rate_area = get_rate_area(zipcode, zips_path) # Use helper function here...
        
        if rate_area:
            logging.info(f"Found rate area {rate_area} for ZIP {zipcode}")
            second_lowest_rate = get_second_lowest_silver_plan(rate_area, plans_path) # Use helper function here...
            
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
