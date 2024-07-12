1) The head() method returns the headers and a specified number of rows, starting from the top.
    * printing the first 10 rows of the DataFrame:
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.head(10))
    * Print the first 5 rows of the DataFrame:
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.head())

2) The tail() method returns the headers and a specified number of rows, starting from the bottom.
      print(df.tail()) 

3) he DataFrames object has a method called info(), that gives you more information about the data set.
      print(df.info()) 

4) Null Values
      Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. 
      This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.

