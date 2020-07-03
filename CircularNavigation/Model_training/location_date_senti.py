# Importing libraries
import pandas as pd

# Loading Datasets
date_sentiment_data = pd.read_csv('Date_Sentiments.csv')
df = pd.read_csv('../Data_collection/COVID-19_Sentiments.csv')

# Creating list of states in India
India_state_list = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
                    'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli',
                    'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                    'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep',
                    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                    'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                    'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
                    ]

## Combining locations with its respective sentiments
Location_list = []
Sentiments_list = []
Date_list = []

for locations, sentiments, dates in zip(df.Location, date_sentiment_data.Sentiments,
                                date_sentiment_data.Date):
    locations = locations.lower().split(',')[0]
    for states in India_state_list:
        states = states.lower()
        if locations == states:
            Location_list.append(states)
            Sentiments_list.append(sentiments)
            Date_list.append(dates)

# To check for Nan values.
location_len = len(Location_list)
sentiments_len = len(Sentiments_list)
date_len = len(Date_list)

if location_len == sentiments_len == date_len:
    print('Your data looks good; No Nan values found')
    print('length--> ', location_len)
    
    # Converting into dataframe and then saving it in form of csv file.
    Location_Sentiments = pd.DataFrame({
        'Location': Location_list,
        'Date': Date_list,
        'Sentiments': Sentiments_list
    })

    print(Location_Sentiments.head())

    Location_Sentiments.to_csv('Location_Date_Sentiments.csv', index=False)

else:
    print('There may exist some Nan values')

