some of the most commonly used operations for managing columns, including how to:

1) Rename columns : 
      Use rename() method of the DataFrame to change the name of a column
          dfnew = df.rename(columns={'popu': 'population'})

2) Add columns :
      You can add a column to DataFrame object by assigning an array-like object (list, ndarray, Series) to a new column using the [ ] operator. 
      This will modify the DataFrame 'in place' (no copy constructed)
          # Add a list as a new column 
              dfnew['capital city'] = ['Rome','Madrid','Athens','Paris','Lisbon']
          # Add an array as a new column 
              ar = np.array([39,34,30,33,351])
              dfnew['Calling code'] = ar
          # Add a Series array as a new column. When adding a Series data are automatically aligned based on index 
              ser = pd.Series(['es','it','fr','pt','gr'], index = ['ESP','ITA','FRA','PRT','GRC'])
              dfnew['Internet domain'] = ser

3) Delete columns :
      # Delete using del 
          del dfnew['Internet domain']
      # Delete using drop() 
          dfdrop = dfnew.drop(['Calling code'], axis=1)

4) Insert/Rearrange columns : 
      Use the insert() method of the DataFrame to insert a column in a specific position
        # Note that the first column is in position with index '0'
              ser = pd.Series(['es','it','fr','pt','gr'], index = ['ESP','ITA','FRA','PRT','GRC'])
              dfnew.insert(1,'Internet domains',ser)

        # Rearrange
          # Get the DataFrame column names as a list
              clist = list(dfnew.columns)
          # Rearrange list the way you like 
              clist_new = clist[-1:]+clist[:-1]   # brings the last column in the first place
          # Pass the new list to the DataFrame - like a key list in a dict 
              dfnew = dfnew[clist_new]

          # Alternatively you can write the column header list the way you like and pass it to the DataFrame object
              clist = ['country','capital city','Internet domains','population','percent','Calling code']
              dfnew = dfnew[clist]


5) Replace column contents :
      Use the [ ] notation to assign new values to a column.
        data = {'country': ['Italy','Spain','Greece','France','Portugal'],
                'popu': [61, 46, 11, 65, 10],
                'percent': [0.83,0.63,0.15,0.88,0.14]}
        df = pd.DataFrame(data, index=['ITA', 'ESP', 'GRC', 'FRA', 'PRT'])
        df.percent = '-'     # A single value 'propagates' to all column cells

        df.percent = 0.001*df.popu   # Data in 'percent' and 'popu' columns are autonatically aligned  
        df


