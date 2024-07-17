import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    newdf = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3',  'quarter_4'])
    dfnew = newdf.rename(columns={'variable': 'quarter', 'value' : 'sales'})

    return dfnew



# -------------------------------------------------
#                   OR 
# -------------------------------------------------

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    newdf = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3',  'quarter_4'], var_name='quarter', value_name='sales')
    return newdf