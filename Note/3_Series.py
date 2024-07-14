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

