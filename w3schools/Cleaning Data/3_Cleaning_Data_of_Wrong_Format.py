                                                                      Cleaning Data of Wrong Format
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: 
    1) remove the rows, 
        * Let's try to convert all cells in the 'Date' column into dates. Pandas has a to_datetime() method for this:
              import pandas as pd
              df = pd.read_csv('data.csv')              
              df['Date'] = pd.to_datetime(df['Date'])              
              print(df.to_string())

    2) convert all cells in the columns into the same format.
        * The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
            import pandas as pd
            df = pd.read_csv('data.csv')
            df['Date'] = pd.to_datetime(df['Date'])
            df.dropna(subset=['Date'], inplace = True)
            print(df.to_string())
