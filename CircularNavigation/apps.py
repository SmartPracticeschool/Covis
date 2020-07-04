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

ls = [table_dict, total_positive, total_negative, total_neutral]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('main.html', ls=ls)

if __name__ == "__main__":
    app.run(debug=True)