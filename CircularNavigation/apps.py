from state_date_senti import state_date_senti_plot
from states_tags import States_tags
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
df3 = pd.read_csv(r'Data_collection/data/COVID-19_Sentiments.csv')

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

# plot for statewise hashtags
state_tags_dict = States_tags(df3)
haryana_tags_plot = plot.tags_barplot(state_tags_dict, 'haryana')

ls = [table_dict, total_positive, total_neutral,
        total_negative, haryana_tags_plot]
ls1 = [phase_1, phase_2, phase_3, phase_4]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('main.html', ls=ls)

@app.route('/four', methods=['POST', 'GET'])
def four(): 
    return render_template('fphase.html', ls1=ls1)

def check_state(state):
    if state == 'Andhra':
        args = [states_dates_dict['andhra pradesh']]
    elif state == 'Arunachal':
        args = [states_dates_dict['arunachal pradesh']]
    elif state == 'Assam':
        args = [states_dates_dict['assam']]
    elif state == 'Bihar':
        args = [states_dates_dict['bihar']]
    elif state == 'Chandigarh':
        args = [states_dates_dict['chandigarh']]
    elif state == 'Chhattisgarh':
        args = [states_dates_dict['chhattisgarh']]
    elif state == 'Dadra and Nagar Haveli':
        args = [states_dates_dict['dadra and nagar haveli']]
    elif state == 'Daman And Diu':
        args = [states_dates_dict['daman and diu']]
    elif state == 'Delhi':
        args = [states_dates_dict['delhi']]
    elif state == 'Goa':
        args = [states_dates_dict['goa']]
    elif state == 'Gujrat':
        args = [states_dates_dict['gujarat']]
    elif state == 'Haryana':
        args = [states_dates_dict['haryana']]
    elif state == 'Himachal':
        args = [states_dates_dict['himachal pradesh']]
    elif state == 'Jammu':
        args = [states_dates_dict['jammu and kashmir']]
    elif state == 'Jharkhand':
        args = [states_dates_dict['jharkhand']]
    elif state == 'Karnataka':
        args = [states_dates_dict['karnataka']]
    elif state == 'Kerala':
        args = [states_dates_dict['kerala']]
    elif state == 'Madhya':
        args = [states_dates_dict['madhya pradesh']]
    elif state == 'Maharashtra':
        args = [states_dates_dict['maharashtra']]
    elif state == 'Manipur':
        args = [states_dates_dict['manipur']]
    elif state == 'Meghalaya':
        args = [states_dates_dict['meghalaya']]
    elif state == 'Mizoram':
        args = [states_dates_dict['mizoram']]
    elif state == 'Nagaland':
        args = [states_dates_dict['nagaland']]
    elif state == 'Odisha':
        args = [states_dates_dict['odisha']]
    elif state == 'Puducherry':
        args = [states_dates_dict['puducherry']]
    elif state == 'Punjab':
        args = [states_dates_dict['punjab']]
    elif state == 'Rajasthan':
        args = [states_dates_dict['rajasthan']]
    elif state == 'Sikkim':
        args = [states_dates_dict['sikkim']]
    elif state == 'Tamil':
        args = [states_dates_dict['tamil nadu']]
    elif state == 'Tripura':
        args = [states_dates_dict['tripura']]
    elif state == 'Uttar':
        args = [states_dates_dict['uttar pradesh']]
    elif state == 'Uttarakhand':
        args = [states_dates_dict['uttarakhand']]
    elif state == 'West':
        args = [states_dates_dict['west bengal']]
    elif state == 'Telangana':
        args = [states_dates_dict['andhra pradesh']]
    
    return args

@app.route('/states', methods=['POST', 'GET'])
def states(): 
    if request.method == 'POST':
        state = request.form['button']
        args = check_state(state)
        return render_template('test.html', args=args)

if __name__ == "__main__":
    app.run(debug=True)
