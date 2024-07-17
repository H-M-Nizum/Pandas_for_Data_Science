Below you can see a simple example of how to use the pd.concat() method to add new rows to a DataFrame

1)  Add rows with 'concat' : 
      pandas offer a powerful 'concat' method to concatenate DataFrames or Series objects
            import numpy as np 
            import pandas as pd
            
            data1 = {'country': ['Italy','Spain','Greece','France','Portugal'],
                    'popu': [61, 46, 11, 65, 10]
                    }
            data2 = {'country': ['Brazil','Argentina'],
                    'popu': [207, 44]
                    }
            
            df1 = pd.DataFrame(data1, index=['ITA', 'ESP', 'GRC', 'FRA', 'PRT'])
            df2 = pd.DataFrame(data2, index=['BRA', 'ARG'])
            total = pd.concat([df2, df1])
