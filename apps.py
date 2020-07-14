from state_date_senti import state_date_senti_plot
from states_tags import States_tags
import plot
import pandas as pd
import numpy as np
from plot import Plot
import os
import tweepy
from textblob import TextBlob
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
total_positive_num = data_plot_dict['total_num_pos']
total_negative_num = data_plot_dict['total_num_neg']
total_neutral_num = data_plot_dict['total_num_neutral']
state_date_senti_dict = state_date_senti_plot(df2)

# function for accessing total number of each sentiments of every phase
def phase_data(pos_list, neg_list, neu_list, name):
    if name == 'Phase 1':
        pos_sum = sum(pos_list[5:24])
        neg_sum = sum(neg_list[5:24])
        neu_sum = sum(neu_list[5:24])
    elif name == 'Phase 2':
        pos_sum = sum(pos_list[24:43])
        neg_sum = sum(neg_list[24:43])
        neu_sum = sum(neu_list[24:43])
    elif name == 'Phase 3':
        pos_sum = sum(pos_list[43:56])
        neg_sum = sum(neg_list[43:56])
        neu_sum = sum(neu_list[43:56])
    elif name == 'Phase 4':
        pos_sum = sum(pos_list[56:70])
        neg_sum = sum(neg_list[56:70])
        neu_sum = sum(neu_list[56:70])
    
    return [pos_sum, neg_sum, neu_sum]


# getting total number for each phase
ph1_pos, ph1_neg, ph1_neu = phase_data(total_positive_num, total_negative_num,
                                        total_neutral_num, 'Phase 1')
ph2_pos, ph2_neg, ph2_neu = phase_data(total_positive_num, total_negative_num,
                                        total_neutral_num, 'Phase 2')
ph3_pos, ph3_neg, ph3_neu = phase_data(total_positive_num, total_negative_num,
                                        total_neutral_num, 'Phase 3')
ph4_pos, ph4_neg, ph4_neu = phase_data(total_positive_num, total_negative_num,
                                        total_neutral_num, 'Phase 4')
    

# Data for tables
table_dict = table_plot(df1)

sunburst_ploted = plot.sunburst_chart(table_dict['Positive_sentiments'],
                                    table_dict['Negative_sentiments'],
                                    table_dict['Neutral_sentiments']
                        )

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
ls1 = [phase_1, phase_2, phase_3, phase_4,
        ph1_pos, ph1_neg, ph1_neu,
        ph2_pos, ph2_neg, ph2_neu,
        ph3_pos, ph3_neg, ph3_neu,
        ph4_pos, ph4_neg, ph4_neu
        ]

@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('main.html', ls=ls)

@app.route('/four', methods=['POST', 'GET'])
def four(): 
    return render_template('fphase.html', ls1=ls1)

def check_state(state):
    if state == 'More About Andhra Pradesh':
        args = [states_dates_dict['andhra pradesh'], andhra_tags_plot,'Andhra Pradesh',"4,97,00,000",list(state_tags_dict['andhra pradesh'].keys()),list(state_tags_dict['andhra pradesh'].values()), table_dict['Positive_sentiments']['andhra pradesh'], table_dict['Negative_sentiments']['andhra pradesh'], table_dict['Neutral_sentiments']['andhra pradesh'], table_dict['Positive_number']['andhra pradesh'], table_dict['Negative_number']['andhra pradesh'], table_dict['Neutral_number']['andhra pradesh']]
    elif state == 'More About Arunachal Pradesh':
        args = [states_dates_dict['arunachal pradesh'], arunachal_tags_plot, 'Arunachal Pradesh', "12,60,000",list(state_tags_dict['arunachal pradesh'].keys()),list(state_tags_dict['arunachal pradesh'].values()), table_dict['Positive_sentiments']['arunachal pradesh'], table_dict['Negative_sentiments']['arunachal pradesh'], table_dict['Neutral_sentiments']['arunachal pradesh'], table_dict['Positive_number']['arunachal pradesh'], table_dict['Negative_number']['arunachal pradesh'], table_dict['Neutral_number']['arunachal pradesh']]
    elif state == 'More About Assam':
        args = [states_dates_dict['assam'], assam_tags_plot, 'Assam', "3,90,00,000",list(state_tags_dict['assam'].keys()),list(state_tags_dict['assam'].values()), table_dict['Positive_sentiments']['assam'], table_dict['Negative_sentiments']['assam'], table_dict['Neutral_sentiments']['assam'], table_dict['Positive_number']['assam'], table_dict['Negative_number']['assam'], table_dict['Neutral_number']['assam']]
    elif state == 'More About Bihar':
        args = [states_dates_dict['bihar'], bihar_tags_plot, 'Bihar',"9,90,00,000",list(state_tags_dict['bihar'].keys()),list(state_tags_dict['bihar'].values()), table_dict['Positive_sentiments']['bihar'], table_dict['Negative_sentiments']['bihar'], table_dict['Neutral_sentiments']['bihar'], table_dict['Positive_number']['bihar'], table_dict['Negative_number']['bihar'], table_dict['Neutral_number']['bihar']]
    elif state == 'More About Chhattisgarh':
        args = [states_dates_dict['chhattisgarh'], chhattisgarh_tags_plot, 'Chhattisgarh',"3,22,00,000",list(state_tags_dict['chhattisgarh'].keys()),list(state_tags_dict['chhattisgarh'].values()), table_dict['Positive_sentiments']['chhattisgarh'], table_dict['Negative_sentiments']['chhattisgarh'], table_dict['Neutral_sentiments']['chhattisgarh'], table_dict['Positive_number']['chhattisgarh'], table_dict['Negative_number']['chhattisgarh'], table_dict['Neutral_number']['chhattisgarh']]
    elif state == 'More About Delhi':
        args = [states_dates_dict['delhi'], delhi_tags_plot, 'Delhi',"1,90,00,000",list(state_tags_dict['delhi'].keys()),list(state_tags_dict['delhi'].values()), table_dict['Positive_sentiments']['delhi'], table_dict['Negative_sentiments']['delhi'], table_dict['Neutral_sentiments']['delhi'], table_dict['Positive_number']['delhi'], table_dict['Negative_number']['delhi'], table_dict['Neutral_number']['delhi']]
    elif state == 'More About Goa':
        args = [states_dates_dict['goa'], goa_tags_plot, 'Goa',"18,20,000",list(state_tags_dict['goa'].keys()),list(state_tags_dict['goa'].values()), table_dict['Positive_sentiments']['goa'], table_dict['Negative_sentiments']['goa'], table_dict['Neutral_sentiments']['goa'], table_dict['Positive_number']['goa'], table_dict['Negative_number']['goa'], table_dict['Neutral_number']['goa']]
    elif state == 'More About Gujrat':
        args = [states_dates_dict['gujarat'], gujarat_tags_plot, 'Gujarat',"6,27,00,000",list(state_tags_dict['gujarat'].keys()), list(state_tags_dict['gujarat'].values()), table_dict['Positive_sentiments']['gujarat'], table_dict['Negative_sentiments']['gujarat'], table_dict['Neutral_sentiments']['gujarat'], table_dict['Positive_number']['gujarat'], table_dict['Negative_number']['gujarat'], table_dict['Neutral_number']['gujarat']]
    elif state == 'More About Haryana':
        args = [states_dates_dict['haryana'], haryana_tags_plot, 'Haryana',"2,54,00,000",list(state_tags_dict['haryana'].keys()), list(state_tags_dict['haryana'].values()), table_dict['Positive_sentiments']['haryana'], table_dict['Negative_sentiments']['haryana'], table_dict['Neutral_sentiments']['haryana'], table_dict['Positive_number']['haryana'], table_dict['Negative_number']['haryana'], table_dict['Neutral_number']['haryana']]
    elif state == 'More About Himachal Pradesh':
        args = [states_dates_dict['himachal pradesh'], himachal_tags_plot, 'Himachal Pradesh',"68,60,000",list(state_tags_dict['himachal pradesh'].keys()), list(state_tags_dict['himachal pradesh'].values()), table_dict['Positive_sentiments']['himachal pradesh'], table_dict['Negative_sentiments']['himachal pradesh'], table_dict['Neutral_sentiments']['himachal pradesh'], table_dict['Positive_number']['himachal pradesh'], table_dict['Negative_number']['himachal pradesh'], table_dict['Neutral_number']['himachal pradesh']]
    elif state == 'More About Jammu and Kashmir':
        args = [states_dates_dict['jammu and kashmir'], jk_tags_plot, 'Jammu and Kashmir',"1,25,00,000",list(state_tags_dict['jammu and kashmir'].keys()), list(state_tags_dict['jammu and kashmir'].values()), table_dict['Positive_sentiments']['jammu and kashmir'], table_dict['Negative_sentiments']['jammu and kashmir'], table_dict['Neutral_sentiments']['jammu and kashmir'], table_dict['Positive_number']['jammu and kashmir'], table_dict['Negative_number']['jammu and kashmir'], table_dict['Neutral_number']['jammu and kashmir']]
    elif state == 'More About Jharkhand':
        args = [states_dates_dict['jharkhand'], jharkhand_tags_plot, 'Jharkhand',"3,19,00,000",list(state_tags_dict['jharkhand'].keys()), list(state_tags_dict['jharkhand'].values()), table_dict['Positive_sentiments']['jharkhand'], table_dict['Negative_sentiments']['jharkhand'], table_dict['Neutral_sentiments']['jharkhand'], table_dict['Positive_number']['jharkhand'], table_dict['Negative_number']['jharkhand'], table_dict['Neutral_number']['jharkhand']]
    elif state == 'More About Karnataka':
        args = [states_dates_dict['karnataka'], karnataka_tags_plot, 'Karnataka',"6,41,00,000",list(state_tags_dict['karnataka'].keys()), list(state_tags_dict['karnataka'].values()), table_dict['Positive_sentiments']['karnataka'], table_dict['Negative_sentiments']['karnataka'], table_dict['Neutral_sentiments']['karnataka'], table_dict['Positive_number']['karnataka'], table_dict['Negative_number']['karnataka'], table_dict['Neutral_number']['karnataka']]
    elif state == 'More About Kerala':
        args = [states_dates_dict['kerala'], kerala_tags_plot, 'Kerala',"3,48,00,000",list(state_tags_dict['kerala'].keys()),list(state_tags_dict['kerala'].values()), table_dict['Positive_sentiments']['kerala'], table_dict['Negative_sentiments']['kerala'], table_dict['Neutral_sentiments']['kerala'], table_dict['Positive_number']['kerala'], table_dict['Negative_number']['kerala'], table_dict['Neutral_number']['kerala']]
    elif state == 'More About Madhya Pradesh':
        args = [states_dates_dict['madhya pradesh'], madhya_tags_plot, 'Madhya Pradesh',"7,33,00,000",list(state_tags_dict['madhya pradesh'].keys()), list(state_tags_dict['madhya pradesh'].values()), table_dict['Positive_sentiments']['madhya pradesh'], table_dict['Negative_sentiments']['madhya pradesh'], table_dict['Neutral_sentiments']['madhya pradesh'], table_dict['Positive_number']['madhya pradesh'], table_dict['Negative_number']['madhya pradesh'], table_dict['Neutral_number']['madhya pradesh']]
    elif state == 'More About Maharashtra':
        args = [states_dates_dict['maharashtra'], maharashtra_tags_plot, 'Maharashtra',"11,42,00,000",list(state_tags_dict['maharashtra'].keys()),list(state_tags_dict['maharashtra'].values()), table_dict['Positive_sentiments']['maharashtra'], table_dict['Negative_sentiments']['maharashtra'], table_dict['Neutral_sentiments']['maharashtra'], table_dict['Positive_number']['maharashtra'], table_dict['Negative_number']['maharashtra'], table_dict['Neutral_number']['maharashtra']]
    elif state == 'More About Manipur':
        args = [states_dates_dict['manipur'], manipur_tags_plot, 'Manipur',"27,20,000",list(state_tags_dict['manipur'].keys()), list(state_tags_dict['manipur'].values()), table_dict['Positive_sentiments']['manipur'], table_dict['Negative_sentiments']['manipur'], table_dict['Neutral_sentiments']['manipur'], table_dict['Positive_number']['manipur'], table_dict['Negative_number']['manipur'], table_dict['Neutral_number']['manipur']]
    elif state == 'More About Meghalya':
        args = [states_dates_dict['meghalaya'], meghalaya_tags_plot, 'Meghalaya',"26,50,000",list(state_tags_dict['meghalaya'].keys()),list(state_tags_dict['meghalaya'].values()), table_dict['Positive_sentiments']['meghalaya'], table_dict['Negative_sentiments']['meghalaya'], table_dict['Neutral_sentiments']['meghalaya'], table_dict['Positive_number']['meghalaya'], table_dict['Negative_number']['meghalaya'], table_dict['Neutral_number']['meghalaya']]
    elif state == 'More About Mizoram':
        args = [states_dates_dict['mizoram'], mizoram_tags_plot, 'Mizoram',"11,20,000",list(state_tags_dict['mizoram'].keys()),list(state_tags_dict['mizoram'].values()), table_dict['Positive_sentiments']['mizoram'], table_dict['Negative_sentiments']['mizoram'], table_dict['Neutral_sentiments']['mizoram'], table_dict['Positive_number']['mizoram'], table_dict['Negative_number']['mizoram'], table_dict['Neutral_number']['mizoram']]
    elif state == 'More About Nagaland':
        args = [states_dates_dict['nagaland'], nagaland_tags_plot, 'Nagaland',"22,80,000",list(state_tags_dict['nagaland'].keys()), list(state_tags_dict['nagaland'].values()), table_dict['Positive_sentiments']['nagaland'], table_dict['Negative_sentiments']['nagaland'], table_dict['Neutral_sentiments']['nagaland'], table_dict['Positive_number']['nagaland'], table_dict['Negative_number']['nagaland'], table_dict['nagaland']['arunachal pradesh']]
    elif state == 'More About Odisha':
        args = [states_dates_dict['odisha'], odisha_tags_plot, 'Odisha',"4,37,00,000",list(state_tags_dict['odisha'].keys()), list(state_tags_dict['odisha'].values()), table_dict['Positive_sentiments']['odisha'], table_dict['Negative_sentiments']['odisha'], table_dict['Neutral_sentiments']['odisha'], table_dict['Positive_number']['odisha'], table_dict['Negative_number']['odisha'], table_dict['Neutral_number']['odisha']]
    elif state == 'More About Punjab':
        args = [states_dates_dict['punjab'], punjab_tags_plot, 'Punjab',"2,08,00,000",list(state_tags_dict['punjab'].keys()), list(state_tags_dict['punjab'].values()), table_dict['Positive_sentiments']['punjab'], table_dict['Negative_sentiments']['punjab'], table_dict['Neutral_sentiments']['punjab'], table_dict['Positive_number']['punjab'], table_dict['Negative_number']['punjab'], table_dict['Neutral_number']['punjab']]
    elif state == 'More About Rajasthan':
        args = [states_dates_dict['rajasthan'], rajasthan_tags_plot, 'Rajasthan',"6,89,00,000",list(state_tags_dict['rajasthan'].keys()), list(state_tags_dict['rajasthan'].values()), table_dict['Positive_sentiments']['rajasthan'], table_dict['Negative_sentiments']['rajasthan'], table_dict['Neutral_sentiments']['rajasthan'], table_dict['Positive_number']['rajasthan'], table_dict['Negative_number']['rajasthan'], table_dict['Neutral_number']['rajasthan']]
    elif state == 'More About Sikkim':
        args = [states_dates_dict['sikkim'], sikkim_tags_plot, 'Sikkim',"06,19,000",list(state_tags_dict['sikkim'].keys()),list(state_tags_dict['sikkim'].values()), table_dict['Positive_sentiments']['sikkim'], table_dict['Negative_sentiments']['sikkim'], table_dict['Neutral_sentiments']['sikkim'], table_dict['Positive_number']['sikkim'], table_dict['Negative_number']['sikkim'], table_dict['Neutral_number']['sikkim']]
    elif state == 'More About Tamil Nadu':
        args = [states_dates_dict['tamil nadu'], tamil_tags_plot, 'Tamil Nadu',"6,79,00,000",list(state_tags_dict['tamil nadu'].keys()),list(state_tags_dict['tamil nadu'].values()), table_dict['Positive_sentiments']['tamil nadu'], table_dict['Negative_sentiments']['tamil nadu'], table_dict['Neutral_sentiments']['tamil nadu'], table_dict['Positive_number']['tamil nadu'], table_dict['Negative_number']['tamil nadu'], table_dict['Neutral_number']['tamil nadu']]
    elif state == 'More About Tripura':
        args = [states_dates_dict['tripura'], tripura_tags_plot, 'Tripura',"36,06,000",list(state_tags_dict['tripura'].keys()), list(state_tags_dict['tripura'].values()), table_dict['Positive_sentiments']['tripura'], table_dict['Negative_sentiments']['tripura'], table_dict['Neutral_sentiments']['tripura'], table_dict['Positive_number']['tripura'], table_dict['Negative_number']['tripura'], table_dict['Neutral_number']['tripura']]
    elif state == 'More About Uttar Pradesh':
        args = [states_dates_dict['uttar pradesh'], uttar_tags_plot, 'Uttar Pradesh',"20,42,00,000",list(state_tags_dict['uttar pradesh'].keys()),
                    list(state_tags_dict['uttar pradesh'].values()), table_dict['Positive_sentiments']['uttar pradesh'], table_dict['Negative_sentiments']['uttar pradesh'], table_dict['Neutral_sentiments']['uttar pradesh'], table_dict['Positive_number']['uttar pradesh'], table_dict['Negative_number']['uttar pradesh'], table_dict['Neutral_number']['uttar pradesh']]
    elif state == 'More About Uttarakhand':
        args = [states_dates_dict['uttarakhand'], uttarakhand_tags_plot, 'Uttarakhand',"1,01,00,000",list(state_tags_dict['uttarakhand'].keys()),
                    list(state_tags_dict['uttarakhand'].values()), table_dict['Positive_sentiments']['uttarakhand'], table_dict['Negative_sentiments']['uttarakhand'], table_dict['Neutral_sentiments']['uttarakhand'], table_dict['Positive_number']['uttarakhand'], table_dict['Negative_number']['uttarakhand'], table_dict['Neutral_number']['uttarakhand']]
    elif state == 'More About West Bengal':
        args = [states_dates_dict['west bengal'], west_tags_plot, 'West Bengal',"9,03,00,000",list(state_tags_dict['west bengal'].keys()),
                    list(state_tags_dict['west bengal'].values()), table_dict['Positive_sentiments']['west bengal'], table_dict['Negative_sentiments']['west bengal'], table_dict['Neutral_sentiments']['west bengal'], table_dict['Positive_number']['west bengal'], table_dict['Negative_number']['west bengal'], table_dict['Neutral_number']['west bengal']]
    elif state == 'More About Telangana':
        args = [states_dates_dict['andhra pradesh'], telangana_tags_plot, 'Telangana',"3,52,00,000",list(state_tags_dict['andhra pradesh'].keys()),
                    list(state_tags_dict['andhra pradesh'].values()), table_dict['Positive_sentiments']['andhra pradesh'], table_dict['Negative_sentiments']['andhra pradesh'], table_dict['Neutral_sentiments']['andhra pradesh'], table_dict['Positive_number']['andhra pradesh'], table_dict['Negative_number']['andhra pradesh'], table_dict['Neutral_number']['andhra pradesh']]
    
    return args

@app.route('/states', methods=['POST', 'GET'])
def states(): 
    if request.method == 'POST':
        state = request.form['button']
        args = check_state(state)
        return render_template('state.html', args=args)

consumer_key = 'BSMhJOk6MGnzDEaHedT769TOp'
consumer_secret = '6dKf8Mog6RQdDPVUxrV8wisnFPfxdPrep4Th3mjUZLtXdZZ3ju'
access_token = '1268458672491040769-p6g1EIKLzWBRwK3jssEjDJY1UvYckr'
access_token_secret = 'SOCMW6iV7UvDjVLEGYyd89sadCjwPKGyjT3IMnSJ6Tu3r'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

list11 = []
list22 = []
list33 = []

new_search = "IndiaFightsCorona+Lockdown -filter:retweets"

tweetsi = tweepy.Cursor(api.search,
                   q=new_search,
                   lang="en",
                   since='2020-07-5').items(10)
for twee in tweetsi:
    tweet_text = (twee.text)
    list22.append(tweet_text)
    day = str((twee.created_at.day))
    month = str((twee.created_at.month))
    year = str((twee.created_at.year))
    time = str(twee.created_at)
    time = str(time[11:])
    dt = (day + '-' + month + '-' + year + '\n' + time)
    list11.append(dt)
    senti = TextBlob(twee.text)
    senti = (senti.sentiment.polarity)
    list33.append(senti)


@app.route('/prediction', methods=['POST', 'GET'])
def prediction(): 
    text = "Enter the tweet!!!"
    if request.method == 'POST':
        message = request.form['message']
        prediction = TextBlob(message)
        prediction = prediction.sentiment.polarity
        if prediction > 0:
            text = f"Sentiment of tweet is positive, {prediction}"
        elif prediction == 0 :
            text = f"Sentiment of tweet is neutral, {prediction}"
        else:
            text = f"Sentiment of tweet is negative, {prediction}"
    return render_template('prediction.html', prediction = text, var=[list11,list22,list33])



lsm = [sunburst_ploted]

@app.route('/dash', methods=['POST', 'GET'])
def dash(): 
    return render_template('dash.html', lsm=lsm)

if __name__ == "__main__":
    app.run(debug=True)
