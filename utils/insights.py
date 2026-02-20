def insights(df):
    print(df.groupby("Item")["Total Spent"].sum().sort_values(ascending=False))
    print(df.groupby("Item")["Payment Method"].count())
    # print(df.groupby(["Item","Payment Method"]).size())
    print("total revenue,", df["Total Spent"].sum())
    print("revenue per location,", df.groupby("Location")["Total Spent"].sum())
