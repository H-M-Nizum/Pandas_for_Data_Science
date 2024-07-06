# Open google colab
# Click file and Mount Drive
# Then copy csv or xlsx path

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/pandas/data1.csv')
print(df)


print('-------------------------------------- Upload file and Import data from Google Colab------------------------------------------------')

from google.colab import files
files.upload()
df1 = pd.read_csv('data1.csv')
print(df1)
