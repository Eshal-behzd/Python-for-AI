import pandas as pd
df  = pd.read_csv('Retail_Sales.csv',  # Read data from a CSV file into a DataFrame
    parse_dates = ['Date'],
    dtype = {
        "Category": "category",
    }
)
df.info() 
# Convert the 'profit' column to numeric type, handling any non-numeric values
df["profit"] = pd.to_numeric(df['profit']) 
df.info()
# Convert city to categorical type
df['City'] = df['City'].astype("category")
df.info()
df['City'].memory_usage(deep=True)  # Check memory usage of the 'City' column
