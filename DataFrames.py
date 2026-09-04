import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('Sales_data.csv')  # Read data from a CSV file into a DataFrame
print("Info:", df.info())  # Print information about the DataFrame

print("Statistical Summary:\n", df.describe())  # Print descriptive statistics of the DataFrame
print("Head:\n", df.head())  # Print the first few rows of the DataFrame
print("Tail:\n", df.tail())  # Print the last few rows of the DataFrame
print("Shape:\n", df.shape)  # Print the shape of the DataFrame (rows, columns)
print("Data Types:\n", df.dtypes)  # Print the data types of each column in the DataFrame
