  import numpy as np
  import pandas as pd

1) Constructing a Series from an array __
      s = pd.Series(np.array([chr(i) for i in range(65,70)]))

2) Accessing Series values __
      un_data = {'Greece':27,
                 'Spain':21,
                 'Italy':20}
      s = pd.Series(un_data) 
      print(s['Greece'])
      print(s['Greece']+uns['Spain'])
      s['Greece'] = 30
      print(s['Greece'])

      OR _____________________________________________________
      s = pd.Series(np.array([chr(i) for i in range(65,70)]))
      print(s[0], s[3]+s[4])
      s[0] = 'NEW'
      s[1] = 'OLD'

3) Series supports vectorized operations __
      s = pd.Series([10,20,30,40,50])
      print(s[s>30])       # printing only Series values > 30 
      print(s*2)           # multiplies all Series data by 2
      print(np.sqrt(s))    # computes the square root of all Series data

-----------------------------------------------------------------------------------------------------------------------------------------------------------
(1) Handling indexes : 
    i) Setting the index -
        Index labels need not be integers. The programmer can set the index labels by passing a list of indexes when constructing the Series object.
          s = pd.Series([10,20,30,40,50], index = ['a','b','c','d','e'])
          print(s['c'])
          x = s['c']+s['a']
          y = s[['b','e']]
          print(x, y)

    ii) Changing index labels when using a dict - 
        When constructing a Series from a dict you can reject the dictionary key labels and assign a new index list for the Series object.
          data = {'a':1,
                  'b':2,
                  'c':3,
                  'd':4,
                  'e':5}
        new_ind = ['A','B','C','D','E']
        s = pd.Series(sorted(data.values()), index=new_ind)

    iii) rename() - 
          If, you need to change specific labels after the Series has been constructed you can use the rename() method, as in the examples below.
              s = s.rename({'a':'A', 'd':'D'})

    iv) reindex() - 
          reindex() works both for Series and DataFrame objects and resets the index labels in these objects. Additionally it offers the functionality of setting default values for new indexes other than NaN.
                    snew = s.reindex(new_ind, fill_value='Unknown')

(2) Handling the 'NaN' (missing) values :
        . Many times data have missing values that are represented as NaN in a Series object
        . Identifying NaN values is easy with the isnull() and notnull() methods
              s = pd.Series(data)
              print(s,'\n')  # Print full series
              print(s.isnull(),'\n') # Print a series contain bool value based on null value
              print(s.notnull())     # Print a series contain bool value based on null value
                                                                                                                                                                                
