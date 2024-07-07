                                                            DataFrames
                                                          --------------
Data sets in Pandas are usually multi-dimensional tables, called DataFrames. Series is like a column, a DataFrame is the whole table.
# DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns. 
  
1) Create a DataFrame from two Series:
    import pandas as pd
    data = {
      "calories": [420, 380, 390],
      "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)
    print(df)
2) Locate Row :
    Pandas use the loc attribute to return one or more specified row(s)
      # Return row 0:
      print(df.loc[0])

      # Return row 0 and 1:
      print(df.loc[[0, 1]])

3) Named Indexes
   # you can name your own indexes.
      import pandas as pd
      data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
      }
      df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
      print(df) 
  # se the named index in the loc attribute to return the specified row(s).
    # Return "day2":
      print(df.loc["day2"])
