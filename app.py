import pandas as pd
import numpy as np
from plot import Plot
from data_plot_labels import data_plot
import plotly.graph_objects as go

# Loading the dataset
df = pd.read_csv('Model_training/Date_Sentiments.csv')

# Creating list of data points
data_plot_dict = data_plot(df)
x_list = data_plot_dict['x_list']
y_list = data_plot_dict['y_list']

# Plot creation
fig = Plot(x_list, y_list)

def lockdown_bar(figure):
    figure.trace_addition(go.Bar,
                        name=['Positive', 'Negative', 'Neutral'],
                        color=['rgb(128,0,128)', 'rgb(26,118,255)', 'rgb(178,34,34)'])

    figure.plotting(title='Sentiments in India',
                    x_title='Dates',
                    y_title='Sentiments',
                    )
    return figure
