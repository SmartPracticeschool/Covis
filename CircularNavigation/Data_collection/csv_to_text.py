'''This is the python file to take only text ids of downloaded data from Ieee-Dataport.org and convert them to text file.
To make it available for hydrator app to fetch tweet texts'''

import pandas as pd

# input csv file
csv_file = input('Enter the name of your input file with extension: ')

# to keep only first row
df = pd.read_csv(csv_file)
df = df.iloc[:, 0]

# converting into txt file
df.to_csv(csv_file[:-4] + '.txt', header=None,
          index=None, sep=' ', mode='a')
