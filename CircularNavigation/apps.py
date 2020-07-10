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
assam_tags_plot = plot.tags_barplot(state_tags_dict, 'assam')
goa_tags_plot = plot.tags_barplot(state_tags_dict, 'goa')
andhra_tags_plot = plot.tags_barplot(state_tags_dict, 'andhra pradesh')
arunachal_tags_plot = plot.tags_barplot(state_tags_dict, 'arunachal pradesh')
bihar_tags_plot = plot.tags_barplot(state_tags_dict, 'bihar')
delhi_tags_plot = plot.tags_barplot(state_tags_dict, 'delhi')
west_tags_plot = plot.tags_barplot(state_tags_dict, 'west bengal')
uttarakhand_tags_plot = plot.tags_barplot(state_tags_dict, 'uttarakhand')
uttar_tags_plot = plot.tags_barplot(state_tags_dict, 'uttar pradesh')
tripura_tags_plot = plot.tags_barplot(state_tags_dict, 'tripura')
telangana_tags_plot = plot.tags_barplot(state_tags_dict, 'andhra pradesh')
tamil_tags_plot = plot.tags_barplot(state_tags_dict, 'tamil nadu')
sikkim_tags_plot = plot.tags_barplot(state_tags_dict, 'sikkim')
rajasthan_tags_plot = plot.tags_barplot(state_tags_dict, 'rajasthan')
punjab_tags_plot = plot.tags_barplot(state_tags_dict, 'punjab')
odisha_tags_plot = plot.tags_barplot(state_tags_dict, 'odisha')
nagaland_tags_plot = plot.tags_barplot(state_tags_dict, 'nagaland')
mizoram_tags_plot = plot.tags_barplot(state_tags_dict, 'mizoram')
meghalaya_tags_plot = plot.tags_barplot(state_tags_dict, 'meghalaya')
manipur_tags_plot = plot.tags_barplot(state_tags_dict, 'manipur')
maharashtra_tags_plot = plot.tags_barplot(state_tags_dict, 'maharashtra')
madhya_tags_plot = plot.tags_barplot(state_tags_dict, 'madhya pradesh')
kerala_tags_plot = plot.tags_barplot(state_tags_dict, 'kerala')
karnataka_tags_plot = plot.tags_barplot(state_tags_dict, 'karnataka')
jharkhand_tags_plot = plot.tags_barplot(state_tags_dict, 'jharkhand')
jk_tags_plot = plot.tags_barplot(state_tags_dict, 'jammu and kashmir')
himachal_tags_plot = plot.tags_barplot(state_tags_dict, 'himachal pradesh')
gujarat_tags_plot = plot.tags_barplot(state_tags_dict, 'gujarat')
chhattisgarh_tags_plot = plot.tags_barplot(state_tags_dict, 'chhattisgarh')

ls = [table_dict, total_positive, total_neutral, total_negative]
ls1 = [phase_1, phase_2, phase_3, phase_4]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('main.html', ls=ls)

@app.route('/four', methods=['POST', 'GET'])
def four(): 
    return render_template('fphase.html', ls1=ls1)

def check_state(state):
    if state == 'Andhra':
        args = [states_dates_dict['andhra pradesh'], andhra_tags_plot, 'Andhra Pradesh', "4,97,00,000"]
    elif state == 'Arunachal':
        args = [states_dates_dict['arunachal pradesh'], arunachal_tags_plot, 'Arunachal Pradesh', "12,60,000"]
    elif state == 'Assam':
        args = [states_dates_dict['assam'], assam_tags_plot, 'Assam', "3,90,00,000"]
    elif state == 'Bihar':
        args = [states_dates_dict['bihar'], bihar_tags_plot, 'Bihar',"9,90,00,000"]
    elif state == 'Chhattisgarh':
        args = [states_dates_dict['chhattisgarh'], chhattisgarh_tags_plot, 'Chhattisgarh',"3,22,00,000"]
    elif state == 'Delhi':
        args = [states_dates_dict['delhi'], delhi_tags_plot, 'Delhi',"1,90,00,000"]
    elif state == 'Goa':
        args = [states_dates_dict['goa'], goa_tags_plot, 'Goa',"18,20,000"]
    elif state == 'Gujrat':
        args = [states_dates_dict['gujarat'], gujarat_tags_plot, 'Gujarat',"6,27,00,000"]
    elif state == 'Haryana':
        args = [states_dates_dict['haryana'], haryana_tags_plot, 'Haryana',"2,54,00,000"]
    elif state == 'Himachal':
        args = [states_dates_dict['himachal pradesh'], himachal_tags_plot, 'Himachal Pradesh',"68,60,000"]
    elif state == 'Jammu':
        args = [states_dates_dict['jammu and kashmir'], jk_tags_plot, 'Jammu and Kashmir',"1,25,00,000"]
    elif state == 'Jharkhand':
        args = [states_dates_dict['jharkhand'], jharkhand_tags_plot, 'Jharkhand',"3,19,00,000"]
    elif state == 'Karnataka':
        args = [states_dates_dict['karnataka'], karnataka_tags_plot, 'Karnataka',"6,41,00,000"]
    elif state == 'Kerala':
        args = [states_dates_dict['kerala'], kerala_tags_plot, 'Kerala',"3,48,00,000"]
    elif state == 'Madhya':
        args = [states_dates_dict['madhya pradesh'], madhya_tags_plot, 'Madhya Pradesh',"7,33,00,000"]
    elif state == 'Maharashtra':
        args = [states_dates_dict['maharashtra'], maharashtra_tags_plot, 'Maharashtra',"11,42,00,000"]
    elif state == 'Manipur':
        args = [states_dates_dict['manipur'], manipur_tags_plot, 'Manipur',"27,20,000"]
    elif state == 'Meghalaya':
        args = [states_dates_dict['meghalaya'], meghalaya_tags_plot, 'Meghalaya',"26,50,000"]
    elif state == 'Mizoram':
        args = [states_dates_dict['mizoram'], mizoram_tags_plot, 'Mizoram',"11,20,000"]
    elif state == 'Nagaland':
        args = [states_dates_dict['nagaland'], nagaland_tags_plot, 'Nagaland',"22,80,000"]
    elif state == 'Odisha':
        args = [states_dates_dict['odisha'], odisha_tags_plot, 'Odisha',"4,37,00,000"]
    elif state == 'Punjab':
        args = [states_dates_dict['punjab'], punjab_tags_plot, 'Punjab',"2,08,00,000"]
    elif state == 'Rajasthan':
        args = [states_dates_dict['rajasthan'], rajasthan_tags_plot, 'Rajasthan',"6,89,00,000"]
    elif state == 'Sikkim':
        args = [states_dates_dict['sikkim'], sikkim_tags_plot, 'Sikkim',"06,19,000"]
    elif state == 'Tamil':
        args = [states_dates_dict['tamil nadu'], tamil_tags_plot, 'Tamil Nadu',"6,79,00,000"]
    elif state == 'Tripura':
        args = [states_dates_dict['tripura'], tripura_tags_plot, 'Tripura',"36,06,000"]
    elif state == 'Uttar':
        args = [states_dates_dict['uttar pradesh'], uttar_tags_plot, 'Uttar Pradesh',"20,42,00,000"]
    elif state == 'Uttarakhand':
        args = [states_dates_dict['uttarakhand'], uttarakhand_tags_plot, 'Uttarakhand',"1,01,00,000"]
    elif state == 'West':
        args = [states_dates_dict['west bengal'], west_tags_plot, 'West Bengal',"9,03,00,000"]
    elif state == 'Telangana':
        args = [states_dates_dict['andhra pradesh'], telangana_tags_plot, 'Telangana',"3,52,00,000"]
    
    return args

@app.route('/states', methods=['POST', 'GET'])
def states(): 
    if request.method == 'POST':
        state = request.form['button']
        args = check_state(state)
        return render_template('state.html', args=args)

if __name__ == "__main__":
    app.run(debug=True)
