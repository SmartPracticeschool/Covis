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

# Plots of different phases
phase_1 = plot.phases_plot(x_list, y_list, 'phase 1')
phase_2 = plot.phases_plot(x_list, y_list, 'phase 2')
phase_3 = plot.phases_plot(x_list, y_list, 'phase 3')
phase_4 = plot.phases_plot(x_list, y_list, 'phase 4')

# Plots for different states
arg1 = state_date_senti_dict['State_date_positive']
arg2 = state_date_senti_dict['State_date_negative']
arg3 = state_date_senti_dict['State_date_neutral']

states_dates_dict = dict()
for states in list(arg1.keys()):
    positive_sentiment = arg1[states]
    negative_sentiment = arg2[states]
    neutral_sentiment = arg3[states]
    states_dates_dict[states] = plot.state_date_plot(positive_sentiment, negative_sentiment,
                                                     neutral_sentiment, states
                                                     )

ls = [table_dict, states_dates_dict]
ls1 = [phase_1, phase_2, phase_3, phase_4]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('main.html', ls=ls)

@app.route('/four', methods=['POST', 'GET'])
def four(): 
    return render_template('fphase.html', ls1=ls1)

if __name__ == "__main__":
    app.run(debug=True)
