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

# Convert date to ISO format with timezone
def convert_date(date_str):
    if pd.isna(date_str):
        return None
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%Y-%m-%dT00:00:00.000Z')

def process_file(input_file, output_file):
    """Process the XLSX file and create the CSV output"""
    logging.info(f"Starting processing of {input_file}")
    
    # Read the watched episodes from Excel file
    # Watched episodes are stored on second sheet
    df = pd.read_excel(input_file, sheet_name=1,nrows=5) # TODO remove debug row limit
    logging.info(f"Loaded {len(df)} rows from Excel file")

    # Create new dataframe with required columns
    selected_columns = ['Сериал', 'Дата просмотра', 'Оценка']
    result_df = pd.DataFrame(columns=[col for col in selected_columns if col in df.columns])

    for index, row in df.iterrows():
        logging.info(f"Processing row {index + 1}/{len(df)}")
        logging.debug(f"Row data: {row.to_dict()}")
        
        id = f"{row['Сериал']} {row['Сезон']} {int(row['Эпизод'])}"
        watched_at = convert_date(row['Дата просмотра'])
        rating = row['Оценка']
        
        # Add to result dataframe
        result_df.loc[index] = [id, watched_at, rating]
        logging.debug(f"Processed values: id={id}, watched_at={watched_at}, rating={rating}")
        
        # Add delay to respect API rate limits
        time.sleep(0.25)
    # Save to CSV
    result_df.to_csv(output_file, index=False)
    logging.info(f"Successfully saved {len(df)} rows to {output_file}")

if __name__ == "__main__":
    input_file = "tv_history.xlsx"
    output_file = "trakt_history.csv"
    logging.info("Starting TV show history conversion")
    process_file(input_file, output_file)
    logging.info("Conversion completed")