#!/usr/bin/python2.7

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
import json
import requests

headers = {'Content-Type': 'application/json'}

loc = r'/usr/akram/soc.csv'
articles = pd.read_csv(loc)

#def geocode(text):
#    article_text = {'text': text}
#    data = json.dumps(article_text)
#    return data

#articles['ab_text'] = articles['AB'].apply(geocode)

def geocode(text):
    article_text = {'text': text}
    data = json.dumps(article_text)
    out = requests.post('http://localhost:5000/country', data=data, headers=headers)
    return out.text

articles['AB_ISO'] = articles['AB'].apply(geocode)

print articles['AB_ISO'].head()



