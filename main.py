import os
import pandas as pd
import logging
from dotenv import load_dotenv
from utils.data_cleaning import data_clean
from utils.read_csv import reading_file
from utils.insights import insights


def setup_logging():
    logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler("app.log")])


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("work started")
    load_dotenv()
    csv_file = os.getenv("input_file")
    df = reading_file(csv_file)
    data_clean(df)
    insights(df)
    current_date = pd.to_datetime("today").strftime("%Y-%m-%d")
    output_file_dated = f"data/{current_date}.csv"
    df.to_csv(output_file_dated)
    logger.info("finished")


if __name__ == "__main__":
    main()
