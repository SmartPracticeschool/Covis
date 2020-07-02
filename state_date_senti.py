# Importing Libraries
import pandas as pd
import numpy as np

def state_date_senti_plot(df):
    # Creating new columns for each sentiments; Positive, Negative, and Neutral
    df['Sentiment_1'] = df['Sentiments'].apply(lambda x: 1 if x == 1 else 0)
    df['Sentiment_neg_1'] = df['Sentiments'].apply(lambda x: 1 if x == -1 else 0)
    df['Sentiment_0'] = df['Sentiments'].apply(lambda x: 1 if x == 0 else 0)
    
    # Accessing different locations...
    locations_list = list(sorted(set([i for i in df['Location']])))
    
    # Creating empty dictionaries; used to update states, dates, and sentiments
    sentiment_1_state_dict = dict()
    sentiment_neg_1_state_dict = dict()
    sentiment_0_state_dict = dict()

    for locations in locations_list:
        for ids in np.where(df.Location == locations):
            sentiment_1_date_dict = dict()
            sentiment_neg_1_date_dict = dict()
            sentiment_0_date_dict = dict()

            df1 = pd.DataFrame(data={
                'Date': df.loc[ids, 'Date'],
                'Sentiments': df.loc[ids, 'Sentiments'],
                'Sentiment_1': df.loc[ids, 'Sentiment_1'],
                'Sentiment_neg_1': df.loc[ids, 'Sentiment_neg_1'],
                'Sentiment_0': df.loc[ids, 'Sentiment_0']
            })
            df1 = df1.reset_index()

            date_list = list(sorted(set([i for i in df1['Date']])))

            for dates in date_list:
                for date_ids in np.where(df1.Date == dates):
                    total_setiments = len(df1.loc[date_ids, 'Sentiments'])
                    total_pos_sentiment = sum(df1.loc[date_ids, 'Sentiment_1'])
                    total_neg_sentiment = sum(df1.loc[date_ids, 'Sentiment_neg_1'])
                    total_neutral_sentiment = sum(df1.loc[date_ids, 'Sentiment_0'])

                    # updates the respective probabilities of sentiments in each dictionaries
                    sentiment_1_date_dict[dates] = round(
                        total_pos_sentiment/total_setiments, 2)
                    sentiment_neg_1_date_dict[dates] = round(
                        total_neg_sentiment/total_setiments, 2)
                    sentiment_0_date_dict[dates] = round(
                        total_neutral_sentiment/total_setiments, 2)

            sentiment_1_state_dict[locations] = sentiment_1_date_dict
            sentiment_neg_1_state_dict[locations] = sentiment_neg_1_date_dict
            sentiment_0_state_dict[locations] = sentiment_0_date_dict


    return dict(State_date_positive = sentiment_1_state_dict,
                State_date_negative = sentiment_neg_1_state_dict,
                State_date_neutral = sentiment_0_state_dict
                )
