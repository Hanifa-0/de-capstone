import pandas as pd
import yaml
import logging

with open("config.yaml", "r") as file:
    configs = yaml.safe_load(file)


def data_clean(df):
    logging.info("data cleaning starts")
    # print(df.count())
    # print(df.isnull().sum())

    # Know about your dataset first
    # print(df.head())
    # print(df.info())
    # print(df.describe())
    # print(df.shape)
    # print(df.dtypes)

    # clean the column name
    # df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
    # print(df.columns)

    # fix data type of column
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
    df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")
    # print(df.dtypes)

    # handle missing values
    df["Quantity"].isnull().sum()
    df["Price Per Unit"].isnull().sum()
    (df["Price Per Unit"].isnull() & df["Quantity"].isnull()).sum()
    df[["Quantity", "Price Per Unit", "Total Spent"]].isnull().sum()

    df.dropna(subset=["Quantity", "Price Per Unit"], inplace=True)
    df.info()
    df[df["Quantity"] * df["Price Per Unit"] != df["Total Spent"]]
    df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]
    df["Total Spent"].isnull().sum()
    # df.info()
    df["Item"] = df["Item"].replace(["UNKNOWN", "ERROR"], pd.NA)
    df.dropna(subset=["Item"], inplace=True)
    df["Payment Method"] = df["Payment Method"].replace("ERROR", pd.NA)
    df.dropna(subset=["Payment Method"], inplace=True)
    df.info()

    print(df["Transaction ID"].duplicated().sum())
    df = df.fillna({"Payment Method": "Unknown"})
    df["Location"] = df["Location"].fillna("Unknown")
    df = df.fillna({"Item": "Unknown"})
    df["Transaction Date"] = df["Transaction Date"].replace("ERROR", pd.NA)
    df["Transaction Date"] = df["Transaction Date"].fillna(pd.Timestamp("2001-10-20"))
    print(df.info())
    print("saving files to: ", configs["files"]["output_file"])
    df.to_csv(configs["files"]["output_file_csv"], index= False)
    df.to_parquet(configs["files"]["output_file"], index=False)
    # print(df.columns)
    # invalid_total = df[
    # df['Total Spent'] != df['Quantity'] * df['Price Per Unit']]
    # print(invalid_total)

    # derived feature
    df["Current Date"] = pd.to_datetime("today")
    df["Days passed after ordering"] = df["Current Date"] - df["Transaction Date"]
    print(df["Days passed after ordering"])

    logging.info("data cleaning done")

    return df
