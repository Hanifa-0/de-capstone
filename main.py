import os
import pandas as pd
from dotenv import load_dotenv
from utils.data_cleaning import data_clean
from utils.read_csv import reading_file
from utils.insights import insights

load_dotenv()
csv_file = os.getenv("input_file")
df = reading_file(csv_file)
data_clean(df)
insights(df)