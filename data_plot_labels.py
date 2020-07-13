import pandas as pd
import numpy as np

def data_plot(df1):
    # Creating new columns of each sentiments
    df1['Sentiment_1'] = df1['Sentiments'].apply(lambda x: 1 if x == 1 else 0)
    df1['Sentiment_neg_1'] = df1['Sentiments'].apply(lambda x: 1 if x == -1 else 0)
    df1['Sentiment_0'] = df1['Sentiments'].apply(lambda x: 1 if x == 0 else 0)

    # Accessing different dates and storing it in the list...
    date_list = list(sorted(set([i for i in df1['Date']])))

    # Creating empty dictionaries; used to update dates along with its probabilities of sentiments
    sentiment_1_dict = dict()
    sentiment_neg_1_dict = dict()
    sentiment_0_dict = dict()
    total_sentiment_1_dict = dict()
    total_sentiment_neg_1_dict = dict()
    total_sentiment_0_dict = dict()

    for dates in date_list:
        for ids in np.where(df1.Date == dates):
            total_setiments = len(df1.loc[ids, 'Sentiments'])
            total_pos_sentiment = sum(df1.loc[ids, 'Sentiment_1'])
            total_neg_sentiment = sum(df1.loc[ids, 'Sentiment_neg_1'])
            total_neutral_sentiment = sum(df1.loc[ids, 'Sentiment_0'])

            # updates the respective probabilities of sentiments in each dictionaries
            sentiment_1_dict[dates] = round(total_pos_sentiment/total_setiments, 3)
            sentiment_neg_1_dict[dates] = round(
                total_neg_sentiment/total_setiments, 3)
            sentiment_0_dict[dates] = round(
                total_neutral_sentiment/total_setiments, 3)
            
            # updating the total number of each sentiments
            total_sentiment_1_dict[dates] = total_pos_sentiment
            total_sentiment_neg_1_dict[dates] = total_neg_sentiment
            total_sentiment_0_dict[dates] = total_neutral_sentiment

    # extracting different x and y data points from their respective dictionaries to plot them on graph
    x1 = list(sentiment_1_dict.keys())
    x2 = list(sentiment_neg_1_dict.keys())
    x3 = list(sentiment_0_dict.keys())
    y1 = list(sentiment_1_dict.values())
    y2 = list(sentiment_neg_1_dict.values())
    y3 = list(sentiment_0_dict.values())

    total_positive = round((sum(list(df1.Sentiment_1)) /len(list(df1.Sentiment_1)))*100, 2)
    total_negative = round((sum(list(df1.Sentiment_neg_1)) /len(list(df1.Sentiment_1)))*100, 2)
    total_neutral = round((sum(list(df1.Sentiment_0)) /len(list(df1.Sentiment_1)))*100, 2)

    return dict(x_list = [x1, x2, x3], y_list = [y1, y2, y3],
                total_positive = total_positive,
                total_negative = total_negative,
                total_neutral = total_neutral,
                total_num_pos = list(total_sentiment_1_dict.values()),
                total_num_neg = list(total_sentiment_neg_1_dict.values()),
                total_num_neutral = list(total_sentiment_0_dict.values())
            )
