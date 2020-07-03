'''It concates all csv files for different dates to one csv file'''
import pandas as pd
import os
import glob

path = r'E:\smart_internz\Data_collection'  # use your path

# give all file names in a particular folder
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

print(concatenated_df.head())

# conversion to one csv file
concatenated_df.to_csv('COVID-19_Sentiments.csv', index=False)
