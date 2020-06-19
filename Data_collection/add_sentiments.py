'''This file is meant for combining sentiments to main data given by tweets_extraction module'''
from tweets_extraction import ExtractTweets
import json
import pandas as pd
import numpy as np

tweets = []
json_file = input('Enter json file with extension: ')
actual_file = input('Enter actual file downloaded from ieee site: ')

for line in open(json_file, encoding="utf8"):
    tweets.append(json.loads(line))

ob = ExtractTweets(tweets)
ob.locate_india()
df = ob.to_dataframe()
name = ob.into_csv(json_file)
print(ob.total_length())
print(df.head())


extracted_data = pd.read_csv(name)
actual_data = pd.read_csv(actual_file, names=['Id', 'Sentiments'])
get_sentiments = pd.read_csv(actual_file, names=[
                            'Id', 'Sentiments'], index_col='Id')


unique_data = extracted_data.drop_duplicates(subset="Text_Id",
                                            keep=False, ignore_index=True)
common_ids = np.intersect1d(actual_data.Id, unique_data.Text_Id)

unique_data_len = len(unique_data)
common_ids_len = len(common_ids)

if unique_data_len == common_ids_len:
    print('Lengths match successfully')

    unique_sentiments = get_sentiments.loc[common_ids]
    unique_sentiments_dic = unique_sentiments.to_dict()

    unique_data['Sentiments'] = unique_data.Text_Id.map(
        unique_sentiments_dic['Sentiments'])

    print(unique_data_len)
    print(unique_data.head())
    unique_data.to_csv(name, index=False)
else:
    print('Lengths are not same, check your code again')
