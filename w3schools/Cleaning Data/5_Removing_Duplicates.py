                                                            Removing Duplicates
------------------------------------------------------------------------------------------------------------------------------------------
Duplicate rows are rows that have been registered more than one time.
To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:
                    import pandas as pd
                    df = pd.read_csv('data.csv')
                    print(df.duplicated())   # Returns True for every row that is a duplicate, otherwise False.

1) Removing Duplicates
    To remove duplicates, use the drop_duplicates() method.
        import pandas as pd
        df = pd.read_csv('data.csv')
        df.drop_duplicates(inplace = True)
        print(df.to_string())

        [NOTE] - The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
