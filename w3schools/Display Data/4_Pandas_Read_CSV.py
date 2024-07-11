# CSV files (comma separated files).CSV files contains plain text and is a well know format.
# Option 1
import pandas as pd
df = pd.read_csv(r'C:\Users\Windows 10 21H2\Downloads\data.csv')
print(df)

# Option 2
import pandas as pd
df = pd.read_csv('C:/Users/Windows 10 21H2/Downloads/data.csv')
print(df)

# Option 3 #### to_string() to print the entire DataFrame.
import pandas as pd
df = pd.read_csv('C:\\Users\\Windows 10 21H2\\Downloads\\data.csv')
# print(df.to_string())

#----------------------------------------------------------------------------------------------------------------

## max_rows
# The number of rows returned is defined in Pandas option settings.
import pandas as pd
print(pd.options.display.max_rows)

#----------------------------------------------------------------------------------------------------------------

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 
