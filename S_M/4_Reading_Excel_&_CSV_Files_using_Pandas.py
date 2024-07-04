# Reading Data From CSV/Excel 
#   1. XLSX (Excel Workbook): 
#       This is a binary file format associated with Microsoft Excel. It can store multiple sheets with formatting, formulas, charts, and images. 
#       More memory and use for large and complex data.
#   2. CSV (Comma-Separated Values): 
#       This is a plain text file where values are separated by commas. It contains only the data without any formatting, formulas, or other elements.
#       less memory and use for small and simple data.

import pandas as pd

print('#------------------------------------------------------- excel file reading -------------------------------------------------------\n')
df = pd.read_excel('data1.xlsx') # If code and excel file store in same folder then don't need to write path. Otherwise write total path.
df1 = pd.read_excel('data1.xlsx', sheet_name = 'Sheet1')
df2 = pd.read_excel('data1.xlsx', sheet_name = 'Sheet2')
print(df)
print(df1)
print(df2)

df4 = pd.read_excel('C:\\Users\\Windows 10 21H2\\Desktop\\Nizum\\Nizum1111\\pandas\\S_M\\data.xlsx')
print(df4)

print('\n#------------------------------------------------------- csv file reading -------------------------------------------------------\n')
df3 = pd.read_csv('data1.csv')
print(df3)
df3 = pd.read_csv('C:\\Users\\Windows 10 21H2\\Downloads\\bike.csv')
print(df3)

