from state_date_senti import state_date_senti_plot
import plot
import pandas as pd
import numpy as np
from plot import Plot
import os
import plotly.graph_objects as go
from data_plot_labels import data_plot
from table_plot_labels import table_plot
from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

# Loading the dataset
df = pd.read_csv(r'Model_training/Date_Sentiments.csv')
df1 = pd.read_csv(r'Model_training/Location_Sentiments.csv')
df2 = pd.read_csv(r'Model_training/Location_Date_Sentiments.csv')

# Creating list of data points for main plots
data_plot_dict = data_plot(df)
x_list = data_plot_dict['x_list']
y_list = data_plot_dict['y_list']
total_positive = data_plot_dict['total_positive']
total_negative = data_plot_dict['total_negative']
total_neutral = data_plot_dict['total_neutral']
state_date_senti_dict = state_date_senti_plot(df2)

# Data for tables
table_dict = table_plot(df1)


## Sunburst plot

# Creating the plot
sunburst_ploted = plot.sunburst_chart(table_dict['Positive_sentiments'],
                                    table_dict['Negative_sentiments'],
                                    table_dict['Neutral_sentiments']
                        )


## Boxplot
# Creating data for the plot
arg1 = state_date_senti_dict['State_date_positive']
arg2 = state_date_senti_dict['State_date_negative']
arg3 = state_date_senti_dict['State_date_neutral']

# Creating the plot
boxplot_states_dict = dict()

for states in list(arg1.keys()):
    y1 = list(arg1[states].values())
    y2 = list(arg2[states].values())
    y3 = list(arg3[states].values())
    boxplot_states_dict[states] = plot.box_plot(y1, y2, y3, states)


## States dates and sentiments plots: Area, Scatter, Line, Bar plots
states_dates_dict = dict()
for states in list(arg1.keys()):
    positive_sentiment = arg1[states]
    negative_sentiment = arg2[states]
    neutral_sentiment = arg3[states]
    states_dates_dict[states] = plot.state_date_plot(positive_sentiment, negative_sentiment,
                                                neutral_sentiment, states
                                            )


##  Main plot creation
fig = Plot(x_list, y_list)

def plot_bar_func(phase):
    if phase == 'p1':
        # used to plot line chart of phase 1 of lockdown in India
        fig.trace_addition(go.Line,
                            name=['Positive 🙂', 'Negative ☹️', 'Neutral 😐'],
                            color=['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-1',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-03-25', '2020-04-14']
                        )
        return plotb
    elif phase == 'p2':
        # used to plot line chart of phase 2 of lockdown in India
        fig.trace_addition(go.Line,
                            name=['Positive 🙂', 'Negative ☹️', 'Neutral 😐'],
                            color=['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-2',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-04-15', '2020-05-3']
                        )
        return plotb
    elif phase == 'p3':
        # used to plot line chart of phase 3 of lockdown in India
        fig.trace_addition(go.Line,
                            name=['Positive 🙂', 'Negative ☹️', 'Neutral 😐'],
                            color=['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-3',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-05-4', '2020-05-17']
                        )
        return plotb
    elif phase == 'p4':
        # used to plot line chart of phase 4 of lockdown in India
        fig.trace_addition(go.Line,
                            name=['Positive 🙂', 'Negative ☹️', 'Neutral 😐'],
                            color=['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-4',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-05-18', '2020-05-31']
                        )
        return plotb

    elif phase == 'p5':
        # used to plot graph of sentiments during full period of lockdown
        plotb = fig.main_plot(go.Line,
                            name=['Positive 🙂', 'Negative ☹️', 'Neutral 😐'],
                            color=['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)'],title='Sentiments of peoples in India During Complete Lockdown',
                        x_title='Dates',
                        y_title='Sentiments',
                        )
        return plotb

    elif phase == 'pie':
        # used to plot pie chart of total percentage of all sentiments during lockdown
        plotb = fig.donnut_pie(title='Lockdown Sentiments of India During Complete Lockdown ,i.e., from 25/March/2020 - 31/May/2020',
                        label= ['Positive Sentiments 🙂', 'Negative Sentiments ☹️', 'Neutral Sentiments 😐'],
                        value= [total_positive, total_negative, total_neutral],
                        center_name= 'Sentiments'
                        )
        return plotb



plotp1 = plot_bar_func('p1')
plotp2 = plot_bar_func('p2')
plotp3 = plot_bar_func('p3')
plotp4 = plot_bar_func('p4')
plotp5 = plot_bar_func('p5')
pie = plot_bar_func('pie')

ls = [plotp1, plotp2, plotp3, plotp4, plotp5, pie,
        sunburst_ploted, boxplot_states_dict, states_dates_dict,
        table_dict
    ]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('home.html', ls=ls)

if __name__ == "__main__":
    app.run(debug=True)
