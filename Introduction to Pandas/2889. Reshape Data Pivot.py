import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    newdf = weather.pivot(index='month', columns='city', values='temperature')
    return newdf