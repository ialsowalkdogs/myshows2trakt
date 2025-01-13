import pandas as pd
from datetime import datetime
import requests
import time
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tv_conversion.log'),
        logging.StreamHandler()
    ]
)

def process_file(input_file, output_file):
    """Process the XLSX file and create the CSV output"""
    logging.info(f"Starting processing of {input_file}")
    
    # Read the watched episodes from Excel file
    # Watched episodes are stored on second sheet
    df = pd.read_excel(input_file, sheet_name=1)
    logging.info(f"Loaded {len(df)} rows from Excel file")
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    logging.info(f"Successfully saved {len(df)} rows to {output_file}")

if __name__ == "__main__":
    input_file = "tv_history.xlsx"
    output_file = "trakt_history.csv"
    logging.info("Starting TV show history conversion")
    process_file(input_file, output_file)
    logging.info("Conversion completed")