import pandas as pd
import requests
from io import StringIO

url = 'https://github.com/rashakil-ds/5-Minutes-to-Pandas/raw/main/Datasets/bike.csv'
response = requests.get(url)

if response.status_code == 200:
    csv_content = response.content.decode('utf-8')  # Read the content of the response as a string

    csv_file = StringIO(csv_content)    # Use StringIO to create a file-like object for pandas

    df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

    # print(df)
    # print(df.head()) # Show only five columns.

else:
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")




#--------------------------- Reading dataset from Github using web get -----------------------------------------
import wget

row_url = 'https://raw.githubusercontent.com/rashakil-ds/5-Minutes-to-Pandas/main/Datasets/bike.csv'
file_path = wget.download(row_url)
df1 = pd.read_csv(file_path)
# print(df1.head())



# ---------------------------------------------Reading dataset from Github using direct raw data URL ---------------------------------------------
direct_url = 'https://raw.githubusercontent.com/rashakil-ds/5-Minutes-to-Pandas/main/Datasets/bike.csv'
df2 = pd.read_csv(direct_url)
# print(df2)
