# create a Series from the list
print("--------------------- Series --------------------")
import pandas as pd
data = [1,2,3,4,5,6,7,8]
s = pd.Series(data)
print(s)
print("Type -- ", type(s))


# Crete a DataFrame from the Series.
print("\n------------------------ DataFrame ----------------------")
df = pd.DataFrame(s)
print(df)
print("Type -- ", type(df))

# If i want add columns name, i can do it
print("\n------------------------ DataFrame : Add columns name ----------------------")
df1 = pd.DataFrame(s, columns=['Age'])
print(df1)


#Create a DataFrame from the list
print("\n------------------------ DataFrame : from list ----------------------")
df2 = pd.DataFrame(data, columns=['Roll'])
print(df2)


# Create a Series from the DataFrame
print("\n------------------------ Series : from DataFrame ----------------------")
s2 = df2['Roll']
print(s2)

# Create a DataFrame from 2 integer columns
print("\n------------------------ DataFrame : from 2 integer columns ----------------------")
data1 = [[1,2], [3,4], [5,6], [7,8]]
df3 = pd.DataFrame(data1, columns=['num1', 'num2'])
print(df3)