# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:14:06 2020

@author: ramesh
"""
#For sentimental analysis


from vaderSentiment.vaderSentiment \
import SentimentIntensityAnalyzer

import pandas as pd


senti = pd.read_csv("final_csv.csv")

analyser = SentimentIntensityAnalyzer()

def sent(text):
        score  = analyser.polarity_scores(text)
        score1 = score["compound"]
        return score1


def Purpose(data):
    purpose = list(senti.iloc[:,1])
    sentiment = list(map(sent,purpose))
    senti['Sentiment_Score'] = sentiment
    senti.sort_values(by=['Sentiment_Score'], inplace=True, ascending=False)
    return senti

senti = Purpose(senti)
top_10 = senti.nlargest(10,['Sentiment_Score'])
top_10.to_csv("Best 10.csv",index=False)
last_10 = senti.nsmallest(10,['Sentiment_Score'])
last_10.to_csv("Last 10.csv",index=False)
