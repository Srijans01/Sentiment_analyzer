import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tkinter import *

import GetOldTweets3 as gt

def get_tweets():
    tweetCriteria = gt.manager.TweetCriteria().setQuerySearch('virat kohli') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-01") \
        .setMaxTweets(1000)
    tweets = gt.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets
txt1=""
text_tweet=get_tweets()
length=len(text_tweet)

for i in range(0,length):
    txt1=text_tweet[i][0] + " " + txt1
    print(txt1)
# txt =open('read.txt',encoding='utf-8').read()


lc=txt1.lower()
ct=lc.translate(str.maketrans('','',string.punctuation))
token_words=word_tokenize(ct,"english")

print(token_words)


final=[]
for w in token_words:
    if w not in stopwords.words('english'):
        final.append(w)

print(final)

emotion_l=[]
with open('emotions.txt','r') as file:
    for l in file:
        clear_l=l.replace("\n",'').replace(",",'').replace("'",'').strip()
        w,e=clear_l.split(':')

        if w in final:
            emotion_l.append(e)

print(emotion_l)
c=Counter(emotion_l)
print(c)

def sentimentfunc(sentiment_t):
    sc=SentimentIntensityAnalyzer().polarity_scores(sentiment_t)
    neg=sc['neg']
    pos=sc['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

    print(sc)

def clearAll() :  
    
    # deleting the content from the entry box  
    negativeField.delete(0, END)  
    neutralField.delete(0, END)  
    positiveField.delete(0, END)  
    overallField.delete(0, END)  
  
    # whole content of text area  is deleted  
    textArea.delete(1.0, END)

f,axis=plt.subplots()
axis.bar(c.keys(),c.values())
f.autofmt_xdate()
plt.savefig('plot.png')
plt.show()