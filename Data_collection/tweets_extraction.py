'''This is used as a module by add_sentiments python file.
    It works on json file extract relevant tweets from that.
    Returns csv file of extracted data.'''
import pandas as pd
import json


class ExtractTweets:
    '''takes in a list of tweets of json format return relevant tweet data based on specified location'''

    def __init__(self, tweets):
        self.tweets = tweets
        self.location = []
        self.id = []
        self.text = []
        self.date = []
        self.total_len = 0

    def locate_india(self):
        '''from different location in original tweet data this only keep necessary tweet data of India'''

        for i in range(len(self.tweets)):
            split_location = self.tweets[i]['user']['location'].split(',')

            for locations in split_location:
                locations = locations.lower().strip()

                if locations == 'india' or locations == 'bharat' or locations == 'mumbai' or locations == 'chennai':
                    self.total_len += 1
                    self.location.append(self.tweets[i]['user']['location'])
                    self.id.append(self.tweets[i]['id_str'])
                    self.date.append(self.tweets[i]['created_at'])
                    self.text.append(self.tweets[i]['full_text'])

    def total_length(self):
        '''returns total length of data'''
        return self.total_len

    def to_dataframe(self):
        '''return data in form of dataframe'''
        self.dataframe = pd.DataFrame({
            'Text_Id': self.id,
            'Text': self.text,
            'Date': self.date,
            'Location': self.location
        })
        
        return self.dataframe
    
    def into_csv(self, json_file_name):
        '''Convert and save dataframe into csv file'''
        name = 'Corona_data' + json_file_name[-8:-5] + '.csv'
        self.dataframe.to_csv(name, index=False)
        return name
