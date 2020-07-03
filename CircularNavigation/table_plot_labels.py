# Importing Libraries
import pandas as pd
import numpy as np


def table_plot(df):
    # Creating new columns for each sentiments; Positive, Negative, and Neutral
    df['Sentiment_1'] = df['Sentiments'].apply(lambda x: 1 if x == 1 else 0)
    df['Sentiment_neg_1'] = df['Sentiments'].apply(
        lambda x: 1 if x == -1 else 0)
    df['Sentiment_0'] = df['Sentiments'].apply(lambda x: 1 if x == 0 else 0)

    # Accessing different locations...
    locations_list = list(sorted(set([i for i in df['Location']])))

    # Creating empty dictionaries; used to update locations along with its probabilities percentage of sentiments
    sentiment_1_dict = dict()
    sentiment_neg_1_dict = dict()
    sentiment_0_dict = dict()

    for locations in locations_list:
        for ids in np.where(df.Location == locations):
            total_setiments = len(df.loc[ids, 'Sentiments'])
            total_pos_sentiment = sum(df.loc[ids, 'Sentiment_1'])
            total_neg_sentiment = sum(df.loc[ids, 'Sentiment_neg_1'])
            total_neutral_sentiment = sum(df.loc[ids, 'Sentiment_0'])

            # updates the respective probabilities percentage of sentiments in each dictionaries
            sentiment_1_dict[locations] = round(
                (total_pos_sentiment/total_setiments)*100, 2)
            sentiment_neg_1_dict[locations] = round(
                (total_neg_sentiment/total_setiments)*100, 2)
            sentiment_0_dict[locations] = round(
                (total_neutral_sentiment/total_setiments)*100, 2)

    return dict(Positive_sentiments = sentiment_1_dict,
                Negative_sentiments = sentiment_neg_1_dict,
                Neutral_sentiments = sentiment_0_dict
                )
