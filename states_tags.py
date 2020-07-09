import pandas as pd
import numpy as np


def States_tags(df):
    ## Creating list of states in India
    India_state_list = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
                        'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana',
                        'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh',
                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab',
                        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
                        ]
    
    
    ## Getting text wrt states
    Location_list = []
    text_list = []
    
    for locations, text in zip(df.Location, df.Text):
        locations = locations.lower().split(',')[0]
        
        
        for states in India_state_list:
            states = states.lower()
            if locations == states:
                Location_list.append(states)
                text_list.append(text)
    
    
    ## Converting into dataframe
    df = pd.DataFrame({'Locations': Location_list,
                        'Text': text_list
                        })
    
    
    ## Getting relevant hashtags
    # Converting to lower case
    df['Text'] = df['Text'].apply(lambda x: x.lower())
    
    # Removing urls
    df['Text'] = df['Text'].apply(lambda x: x.split('https')[0])
    df['Text'] = df['Text'].apply(lambda x: x.split('http')[0])
    
    def func(x):
        try:
            return x.split('#')[1].split(' ')[0]
        except:
            return None
    
    # Column for hashtags
    df['Hash_tags'] = df['Text'].apply(lambda x: func(x))
    
    
    # Removing unwanted char
    df['Hash_tags'] = df['Hash_tags'].str.replace(
        "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ")
    
    
    ## Getting required result (Top 5 repeated hashtags)
    # Accessing different locations...
    locations_list = list(sorted(set([i for i in df.Locations])))
    
    # Creating empty dictionary; used to update locations along with its relevant hashtags
    state_tags_dict = dict()
    
    for locations in locations_list:
        tags_count_dict = dict(
            df[df.Locations == locations].Hash_tags.value_counts().head())
        state_tags_dict[locations] = tags_count_dict
    
    return state_tags_dict
