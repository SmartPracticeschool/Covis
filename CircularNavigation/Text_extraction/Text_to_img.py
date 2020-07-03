# Importing Libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from os import path
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
nltk.download('wordnet')

# Loading Dataset
dataset = pd.read_csv('Data_collection/COVID-19_Sentiments.csv')
print(dataset.head())

# Removing urls
dataset['Text'] = dataset['Text'].apply(lambda x: x.split('https')[0])
dataset['Text'] = dataset['Text'].apply(lambda x: x.split('http')[0])

# Cleaning the text
def func(x):
    try:
        trial = x.split(':')[1]
        return trial
    except:
        return x
dataset['Text'] = dataset['Text'].apply(lambda x: func(x))

# Remove @username
dataset['Text'] = dataset['Text'].str.replace(r'@[^\s]+', '')

# Converting #word into just word
dataset['Text'] = dataset['Text'].str.replace('#', '')

# Fetch wordcount for each abstract
dataset['word_count'] = dataset['Text'].apply(lambda x: len(str(x).split(" ")))
print(dataset[['Text', 'word_count']].head())

## Descriptive statistics of word counts
print(dataset.word_count.describe())

# Identify common words
freq = pd.Series(' '.join(dataset['Text']).split()).value_counts()[:20]
print('Most common words:-\n', freq)

# Identify uncommon words
freq1 = pd.Series(' '.join(dataset['Text']).split()).value_counts()[-20:]
print('Most uncommon words:-\n', freq1)

## Creating a list of stop words and adding custom stopwords
stop_words = set(stopwords.words("english"))

## Creating a list of custom stopwords
new_words = ["using", "show", "result", "large", "also",
            "iv", "one", "two", "new", "previously", "shown"]
stop_words = stop_words.union(new_words)

# Corpus creation
corpus = []
for i in range(0, 648958):
    # Remove punctuations
    text = re.sub('[^a-zA-Z]', ' ', dataset['Text'][i])

    # Convert to lowercase
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # Remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)

    ## Convert to list from string
    text = text.split()

    ## Stemming
    ps = PorterStemmer()
    # Lemmatisation
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if not word in
            stop_words]
    text = " ".join(text)
    corpus.append(text)

#Word cloud
wordcloud = WordCloud(background_color='white',
                    stopwords=stop_words,
                    max_words=100,
                    max_font_size=50,
                    random_state=42
                ).generate(str(corpus))
print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word2.jpg", dpi=900)
