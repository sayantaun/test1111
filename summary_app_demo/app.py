import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import string
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pyLDAvis
import pyLDAvis.gensim
import warnings
warnings.filterwarnings("ignore")
import urllib
from bs4 import BeautifulSoup
import requests

'''Get the summary of the text'''

def get_summary(text, pct):
    summary = summarize(text,ratio=pct,split=True)
    return summary

'''Get the keywords of the text'''

def get_keywords(text):
    res = keywords(text, ratio=0.1, words=None, split=False, scores=False, pos_filter=('NN', 'JJ'), lemmatize=True, deacc=False)
    res = res.split('\n')
    return res

'''Get the text from URL'''

def extract_title_text(url):
    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,'lxml')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    string_features = [x for x in request.form.values()][0]
    title, text = extract_title_text(string_features)
    summary_list = get_summary(text,0.2)
    summary = ''
    for s in summary_list:
        summary += s

    keywords = get_keywords(text)

    return render_template('index.html', searched_url=string_features, prediction_title=title, prediction_summary=summary, prediction_keywords=keywords)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
