import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Salary': [70000, 80000, 60000, 90000, 75000]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# labeled based selection (.loc)
subset_loc = df.loc[df['Age'] > 25, ['Name', 'City']]  # Select rows where Age > 25 and only the Name and City columns
print("\nSubset using loc:\n", subset_loc)
subset_df = df.loc[1:2, ['Name', 'Salary']]  # Select rows 1 to 2 and only the Name and Salary columns
print("\nSubset using DataFrame slicing:\n", subset_df)
# integer based selection (.iloc)
subset_iloc = df.iloc[1:4, [0, 2]]  # Select rows 1 to 3 and only the Name and City columns using integer-based indexing
print("\nSubset using iloc:\n", subset_iloc)
# Boolean Filtering
boolean_filter = df[df['Salary'] > 75000]  # Filter rows where Salary is greater than 75000
print("\nBoolean Filtering:\n", boolean_filter)
# Safe assignment using .loc
df.loc[df['Age'] > 25, 'Salary'] = 85000  # Update the Salary column for rows where Age > 25
print("\nDataFrame after safe assignment:\n", df)
