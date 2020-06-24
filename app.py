import pandas as pd
import numpy as np
from plot import Plot
import plotly.graph_objects as go

# Loading the dataset
df1 = pd.read_csv('Model_training/Date_Sentiments.csv')
print('initial data:-\n', df1.head())

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

print('Final Data:-\n', df1.head())

# extracting different x and y data points from their respective dictionaries to plot them on graph
x1 = list(sentiment_1_dict.keys())
x2 = list(sentiment_neg_1_dict.keys())
x3 = list(sentiment_0_dict.keys())
y1 = list(sentiment_1_dict.values())
y2 = list(sentiment_neg_1_dict.values())
y3 = list(sentiment_0_dict.values())

x_list = [x1, x2, x3]
y_list = [y1, y2, y3]

fig = Plot(x_list, y_list)

fig.trace_addition(go.Bar,
                    name=['Positive', 'Negative', 'Neutral'],
                    color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

fig.plotting(title='Sentiments in India',
                x_title='Dates',
                y_title='Sentiments',
                x_range=['2020-05-18', '2020-05-31']
                )
