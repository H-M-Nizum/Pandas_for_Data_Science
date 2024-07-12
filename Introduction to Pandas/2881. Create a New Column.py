import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create  a new columns and new data based on salary using assign funvtion
    df = employees.assign(bonus=[x*2 for x in list(employees['salary'])])
    return df