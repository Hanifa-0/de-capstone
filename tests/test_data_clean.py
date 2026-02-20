import pandas as pd
from utils.data_cleaning import data_clean


def sample_df():
    return pd.DataFrame(
        {
            "Transaction ID": [2, 3, 4, 5],
            "Item": ["Coffee", "ERROR", "Tea", "Biscuit"],
            "Quantity": ["4", "9", "7", "ERROR"],
            "Price Per Unit": [2, 5, "ERROR", 8],
            "Total Spent": [8, 32, 90, "ERROR"],
            "Payment Method": ["UNKNOWN", "Credit Card", "Cash", "Digital Wallet"],
            "Location": ["Takeaway", "In-store", "In-store", "UNKNOWN"],
            "Transaction Date": ["2001-10-20", "2023-11-15", "ERROR", "2008-12-9"],
        }
    )


def test_data_type_of_columns():
    df = sample_df()
    cleaned_df = data_clean(df)
    assert cleaned_df["Transaction Date"].dtype == "datetime64[us]"
    assert cleaned_df["Quantity"].dtype == "float64"


def test_missing_values():
    df = sample_df()
    cleaned_df = data_clean(df)
    assert cleaned_df.isnull().sum().sum() == 0


def test_replace_error_in_date_column():
    df = sample_df()
    cleaned_df = data_clean(df)
    assert df["Transaction Date"].values != ["ERROR"]
