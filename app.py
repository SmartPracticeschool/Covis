import pandas as pd
import numpy as np
from plot import Plot
import plotly.graph_objects as go
from data_plot_labels import data_plot
from table_plot_labels import table_plot
from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

# Loading the dataset
df = pd.read_csv('Model_training/Date_Sentiments.csv')
df1 = pd.read_csv(r'Model_training/Location_Sentiments.csv')

# Creating list of data points
data_plot_dict = data_plot(df)
x_list = data_plot_dict['x_list']
y_list = data_plot_dict['y_list']
total_positive = data_plot_dict['total_positive']
total_negative = data_plot_dict['total_negative']
total_neutral = data_plot_dict['total_neutral']

# Creating lists for table points
table_plot_dict = table_plot(df1)
Locations = table_plot_dict['Location_list']
Positive_sentiment = table_plot_dict['Positive_sentiments']
Negative_sentiment = table_plot_dict['Negative_sentiments']
Neutral_sentiment = table_plot_dict['Neutral_sentiments']

# Plot creation
fig = Plot(x_list, y_list)

def plot_bar_func(phase):
    if phase == 'p1':
        fig.trace_addition(go.Line,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-1',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-03-25', '2020-04-14']
                        )
        return plotb
    elif phase == 'p2':
        fig.trace_addition(go.Line,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-2',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-04-15', '2020-05-3']
                        )
        return plotb
    elif phase == 'p3':
        fig.trace_addition(go.Line,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-3',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-05-4', '2020-05-17']
                        )
        return plotb
    elif phase == 'p4':
        fig.trace_addition(go.Line,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Phase-4',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-05-18', '2020-05-31']
                        )
        return plotb

    elif phase == 'p5':
        fig.trace_addition(go.Bar,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Complete Lockdown ,i.e., from 25/March/2020 - 31/May/2020',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-03-25', '2020-05-31']
                        )
        return plotb
    
    elif phase == 'l1':
        fig.trace_addition(go.Line,
                            name=['Positive', 'Negative', 'Neutral'],
                            color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

        plotb = fig.plotting(title='Lockdown Sentiments of India During Complete Lockdown ,i.e., from 25/March/2020 - 31/May/2020',
                        x_title='Dates',
                        y_title='Sentiments',
                        x_range=['2020-03-25', '2020-05-31']
                        )
        return plotb
    
    elif phase == 'pie':
        plotb = fig.donnut_pie(title='Lockdown Sentiments of India During Complete Lockdown ,i.e., from 25/March/2020 - 31/May/2020',
                        label= ['Positive Sentiments', 'Negative Sentiments', 'Neutral Sentiments'],
                        value= [total_positive, total_negative, total_neutral],
                        center_name= 'Sentiments'
                        )
        return plotb

def table(figure, locations, positive, negative, neutral):
    final_plot = figure.create_table(locations,
                            positive,
                            negative,
                            neutral,
                            'Lockdown Sentiments in different states during complete lockdown ,i.e., from 25/March/2020 - 31/May/2020')
    return final_plot 

ptable = table(fig, Locations, Positive_sentiment, Negative_sentiment, Neutral_sentiment)

plotp1 = plot_bar_func('p1')
plotp2 = plot_bar_func('p2')
plotp3 = plot_bar_func('p3')
plotp4 = plot_bar_func('p4')
plotp5 = plot_bar_func('p5')
plotl1 = plot_bar_func('l1')
pie = plot_bar_func('pie')

ls = [plotp1, plotp2, plotp3, plotp4, plotp5, plotl1, pie, ptable]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('home.html', ls=ls)

if __name__ == "__main__":
    app.run(debug=True)
