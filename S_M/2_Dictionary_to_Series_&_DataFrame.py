import pandas as pd

data = {
    'name' : ['Akib', 'Sakib', 'Rakib'],
    'age' : [23,24,25],
    'city' : ['Dhaka', 'Mymensingh', 'Kushtia']
}

print(data)

#  create a Series from the Dictionary
print("--------------------- Series --------------------")
s = pd.Series(data, name='series data')
print(s)

#  create a Series from the Dictionary particular key-value
print("--------------------- Series : Dictionary particular key-value --------------------")
s1 = pd.Series(data['name'], name='series data - Name')
print(s1)

# Create a DataFrame from the Dictionary
print("--------------------- DataFrame --------------------")
df = pd.DataFrame(data)
print(df)


# Create a Series from the DataFrame columns
print("--------------------- Series : DataFrame columns --------------------")
age_series = df['age']
print(age_series)
