import pandas as pd
s = pd.Series([1, 3, 4, 6, 8] , index = ['a', 'b', 'c', 'd', 'e'])
print(s)  # Print the Series

print("Values:" , s.values)
print("Index:" , s.index)
print("DataType:" , s.dtype)
print("count", s.value_counts())
# heads() : displays the first n rows of the Series (default is 5)
print("heads:", s.head())
# tails() : displays the last n rows of the Series (default is 5)
print("tails:", s.tail())

