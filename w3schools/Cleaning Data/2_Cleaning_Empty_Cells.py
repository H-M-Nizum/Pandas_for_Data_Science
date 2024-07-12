import pandas as pd
df = pd.read_csv(r'C:\Users\Windows 10 21H2\Downloads\data.csv')
print(df.to_string())

# OUTPUT
#      Duration  Pulse  Maxpulse  Calories
# 0        60.0  110.0     130.0     409.1
# 1        60.0  117.0     145.0     479.0
# 2        60.0  103.0     135.0     340.0
# 3        45.0  109.0     175.0     282.4
# 4        45.0  117.0     148.0     406.0
# 5        60.0  102.0     127.0     300.0
# 6        60.0  110.0     136.0     374.0
# 7        45.0  104.0     134.0     253.3
# 8         NaN  109.0     133.0     195.1
# 9        60.0   98.0     124.0     269.0
# 10       60.0    NaN     147.0     329.3
# 11       60.0  100.0     120.0     250.7
# 12       60.0  106.0       NaN     345.3
# 13       60.0  104.0     132.0       NaN
# 14       60.0   98.0     123.0     275.0
# 15       60.0   98.0     120.0     215.2
# 16       60.0  100.0     120.0     300.0
# 17       45.0   90.0     112.0       NaN
# 18       60.0  103.0     123.0     323.0
# 19       45.0   97.0     125.0     243.0
# 20       60.0  108.0     131.0     364.2

#-------------------------------------- After Empty data cleaning ----------------------------------------
new_df = df.dropna()  # Remove empty cells
print(new_df.to_string())

# By default, the dropna() method returns a new DataFrame, and will not change the original.
# OUTPUT
#      Duration  Pulse  Maxpulse  Calories
# 0        60.0  110.0     130.0     409.1
# 1        60.0  117.0     145.0     479.0
# 2        60.0  103.0     135.0     340.0
# 3        45.0  109.0     175.0     282.4
# 4        45.0  117.0     148.0     406.0
# 5        60.0  102.0     127.0     300.0
# 6        60.0  110.0     136.0     374.0
# 7        45.0  104.0     134.0     253.3
# 9        60.0   98.0     124.0     269.0
# 11       60.0  100.0     120.0     250.7
# 14       60.0   98.0     123.0     275.0
# 15       60.0   98.0     120.0     215.2
# 16       60.0  100.0     120.0     300.0
# 18       60.0  103.0     123.0     323.0
# 19       45.0   97.0     125.0     243.0
# 20       60.0  108.0     131.0     364.2

#-------------------------------
# If you want to change the original DataFrame, use the inplace = True argument:
                                                                        df.dropna(inplace = True)
# Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.



#-------------------------------------- After Replace Empty Values cleaning ---------------------------------------------------------

# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

df.fillna(130, inplace = True)
print(df.to_string())

# OUTPUT 
#  Duration  Pulse  Maxpulse  Calories
# 0        60.0  110.0     130.0     409.1
# 1        60.0  117.0     145.0     479.0
# 2        60.0  103.0     135.0     340.0
# 3        45.0  109.0     175.0     282.4
# 4        45.0  117.0     148.0     406.0
# 5        60.0  102.0     127.0     300.0
# 6        60.0  110.0     136.0     374.0
# 7        45.0  104.0     134.0     253.3
# 8       130.0  109.0     133.0     195.1
# 9        60.0   98.0     124.0     269.0
# 10       60.0  130.0     147.0     329.3
# 11       60.0  100.0     120.0     250.7
# 12       60.0  106.0     130.0     345.3
# 13       60.0  104.0     132.0     130.0
# 14       60.0   98.0     123.0     275.0
# 15       60.0   98.0     120.0     215.2
# 16       60.0  100.0     120.0     300.0
# 17       45.0   90.0     112.0     130.0
# 18       60.0  103.0     123.0     323.0
# 19       45.0   97.0     125.0     243.0
# 20       60.0  108.0     131.0     364.2


#-------------------------------------- Replace Only For Specified Columns ---------------------------------------------------------

# The example above replaces all empty cells in the whole Data Frame. To only replace empty values for one column, specify the column name for the DataFrame:
    df["Calories"].fillna(130, inplace = True)
    
    
#-------------------------------------- Replace Using Mean, Median, or Mode ---------------------------------------------------------
1) Mean = the average value (the sum of all values divided by number of values).
    x = df["Calories"].mean()
    df["Calories"].fillna(x, inplace = True)
    
2) Median = the value in the middle, after you have sorted all values ascending.
    x = df["Calories"].median()
    df["Calories"].fillna(x, inplace = True)
    
3) Mode = the value that appears most frequently.
    x = df["Calories"].mode()[0]
    df["Calories"].fillna(x, inplace = True)


