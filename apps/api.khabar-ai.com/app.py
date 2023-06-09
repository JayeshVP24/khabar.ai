from io import BytesIO
from flask import Flask, jsonify
import os
# import tweepy
from dotenv import load_dotenv
from flask import request,jsonify
import snscrape.modules.twitter as snstwitter
import requests
from goose3 import Goose
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import json
import plotly
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import base64
import pandas as pd
# from flask import send_file
from flask import send_file
import datetime
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging
import sys
from llama_index import GPTVectorStoreIndex, TwitterTweetReader
import os
import llama_index
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import serpapi
from serpapi import GoogleSearch
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv

from flask_cors import CORS
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
import llama_index

import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns



app = Flask(__name__)
CORS(app)
twitterData = None
queryString = None

# print(type(twitterData))

load_dotenv()

print(os.getenv("HUGGINGFACE_API"))
print(os.getenv('OPENAI_API_KEY'))
print(os.getenv('BEARER_TOKEN'))


os.getenv('OPENAI_API_KEY')

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/twitter')
def twitter():
    query = request.args['query']
    retweet = 0
    likecount = 0
    hashtags = set([])
    i=0
    global twitterData
    global queryString
    print("Url: Twitter, data: ", twitterData)
    print("Url: Twitter, query: ", queryString)
    twitterData = snstwitter.TwitterSearchScraper(query).get_items()
        
    for tweet in twitterData: 
        print("looping through tweets")
        print(vars(tweet)) 
        likecount += tweet.likeCount
        retweet += tweet.retweetCount + tweet.quoteCount
        if(tweet.hashtags != None):
            for h in tweet.hashtags:
                hashtags.add(h)
        
        i+= 1
        
        if(i==200):
            break
        
    tweets = {"likecount":likecount,"retweet":retweet,"hashtags":list(hashtags),"count":i}
    print(tweets)
    return jsonify({'result':tweets})
os.getenv('SERPAPI_API_KEY')
#For getting the realted link - by providing the URL
@app.route('/search', methods=['GET'])
def search():
    article_url = request.args.get('url')
    response = requests.get(article_url)
    soup = BeautifulSoup(response.url, 'html.parser')

    header = soup.find('h1').url.strip()
    search_query = quote(header)

    params = {
        'q': search_query,
        'hl': 'en',
        'gl': 'us',
        'api_key': os.getenv('SERPAPI_API_KEY')
    }

    search = GoogleSearch(params)
    results = search.get_dict().get('organic_results', [])

    links = [result['link'] for result in results]

    return jsonify({'article_header': header, 'related_links': links})

# To use LLM to check the factual accuracy of the news
@app.route('/classify_news', methods=['GET'])
def classify_news():

    prompt = request.args['url']

    tool_names = ["serpapi"]
    tools = load_tools(tool_names)

    title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='To classify the news: {topic} in to the categories like murder, fire, accident, natural disaster, etc'
)

#     script_template = PromptTemplate(
#     input_variables = ['title', 'wikipedia_research'], 
#     #template='Look for the authenticity and the accuracy of the news listed: {title} provide the explanation of whether it is factually correct or is there any information present on wikipedia and also provide the correct answer or result if there is:{wikipedia_research} '
#     template='Please verify the authenticity and accuracy of the news provided in the {title} by cross-referencing it with the corresponding {wikipedia_research} page. Examine the information available on Wikipedia and determine whether the news is factually correct or accurate. Additionally, if there is any conflicting or misleading information, please provide the correct answer or result based on your research from Wikipedia. '
# )

    title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
    # script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

    llm = OpenAI(temperature=0.9) 
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
    # script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    # wiki = WikipediaAPIWrapper()
    
    if prompt: 
        title = title_chain.run(prompt)
        a=agent.run(f"{prompt}. Also, provide the realted links")

    return {
        'title': title_memory.buffer,
        'script': a
    }

@app.route('/xyz')
def xyz():
    query = request.args['query']
    tweets = []
    for tweet in snstwitter.TwitterProfileScraper(query).get_items():
        tweets.append(tweet.date)
    return tweets



API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer " +  os.getenv('HUGGINGFACE_API') }
API_URL_PROP = "https://api-inference.huggingface.co/models/valurank/distilroberta-propaganda-2class"
API_URL_HATE = "https://api-inference.huggingface.co/models/IMSyPP/hate_speech_en"



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def queryprop(payload):
	response = requests.post(API_URL_PROP, headers=headers, json=payload)
	return response.json()

def query_hate(payload):
	response = requests.post(API_URL_HATE, headers=headers, json=payload)
	return response.json()



@app.route('/sentiment')
def sentiment():
    query = request.args['query']
    retweet = 0
    likecount = 0
    hashtags = []
    senti=[]
    i=0
    positive=0
    negative=0
    neutral=0
    global twitterData
    global queryString
    print("Url: Sentiment, data: ", twitterData)
    
    twitterData = snstwitter.TwitterSearchScraper(query).get_items()
        
    for tweet in twitterData: 
        if tweet.lang=="en":
            i+=1
            if(i==200):
                break
            sentence= tweet.rawContent
            print(sentence)
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores([sentence])
            print(sentiment_dict['neg']*100, "% Negative")
            print(sentiment_dict['pos']*100, "% Positive")
            print("Review Overall Analysis", end = " ") 
            if sentiment_dict['compound'] >= 0.05 :
                positive+=1
            elif sentiment_dict['compound'] <= -0.05 :
                negative+=1
            else :
                neutral+=1
    senti={"positive":positive, "negative":negative, "neutral":neutral}
    labels = list(senti.keys())
    values = list(senti.values())
        
    data = {"Target": ["Positive","Negative", "Neutral"], "Value": [positive, negative, neutral]}
    df = pd.DataFrame(data)

    target=["Positive","Negative", "Neutral"]
    value=[positive, negative, neutral]

    # palette_color = sns.color_palette('bright')
    #plt.pie(value, labels=target, colors=palette_color, autopct='%.0f%%')
    sns.barplot(x="Target" , y="Value", data=df, palette="Set2")
    plt.title("Sentiment Analysis on the Tweets related to Article")

    plt.savefig('senti.png')

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")

    # print(base64_string)
    # return base64_string

    # fig = plt.gcf()

    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")

    # print(base64_string)
    # return base64_string
    # # return {"labels":labels, "values":values}

    return send_file("./senti.png", mimetype='image/png')


            
@app.route('/sentiment_article')
def sentiment_article():
    senti=[]
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    sentence1 = articles.cleaned_text
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores([sentence1])
    print(sentiment_dict['neg']*100, "% Negative")
    print(sentiment_dict['pos']*100, "% Positive")
    print("Review Overall Analysis", end = " ") 
    if sentiment_dict['compound'] >= 0.05 :
        senti.append("Positive")
    elif sentiment_dict['compound'] <= -0.05 :
        senti.append("Negative")
    else :
        senti.append("Neutral")
    return jsonify({"result":senti,"pos":sentiment_dict})


@app.route('/summary')
def summary():
    try:

        url = request.args['url']
        goose = Goose()
        articles = goose.extract(url)
        output = query({
        "inputs":  articles.cleaned_text
        })
        print(output)
    except:
        return "Please put the relevant url article"

    return jsonify({"result": output[0]['summary_text']})

@app.route('/cloud2')
def plotly_wordcloud2():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    url = articles.cleaned_text
    wordcloud = WordCloud(width=1280, height=853, margin=0,
                      colormap='Blues').generate(url)
    wordcloud.to_file("./wordcloud.png")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")

    # print(base64_string)
    # return base64_string

    return send_file("./wordcloud.png", mimetype='image/png')
    

    
@app.route('/propaganda')
def propaganda():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    output = queryprop({
	"inputs":  articles.cleaned_text[0:600]
    })
    
    yes = output[0][0]['score']
    no = 1 - yes
    
    data = {"Target": ["Propagandastic","Non-Propagandastic"], "Value": [yes, no]}
    df = pd.DataFrame(data)
    sns.barplot(x="Target" , y="Value", data=df, palette="Set2")
    plt.title("Propagandastic Evaluation of the Article")

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")
    plt.savefig('propaganda.png')

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")

    # print(base64_string)
    # return base64_string

    return send_file("./propaganda.png", mimetype='image/png')

    # return base64_string
    # return jsonify({"yes": yes, "no": no})


@app.route("/chat", methods=["GET"])
def chat():
    # Get the query from the request body.
    query = request.args['url']
    # create an app in https://developer.twitter.com/en/apps
    # create reader, specify twitter handles
    reader = TwitterTweetReader(os.getenv('BEARER_TOKEN'))
    documents = reader.load_data(["ANI"])
    documents1 = reader.load_data(["ZeeNews"])
    documents2 = reader.load_data(["TV9Bharatvarsh"])
    documents3 = reader.load_data(["Republic_Bharat"])
    documents4 = reader.load_data(["AajTak"])
    
    # Create a new instance of the llama chatbot agent.
    agent = llama_index.GPTVectorStoreIndex.from_documents(documents1+documents+documents2+documents3+documents4)
    chat_engine = agent.as_chat_engine(verbose=True)

    # Get the response from the llama chatbot agent.
    response = chat_engine.chat(query)

    # Return the response as JSON.
    return jsonify({"response": response})


@app.route('/hate-speech')
def hate():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    url = articles.cleaned_text
    analyzer = SentimentIntensityAnalyzer() 
        # the object outputs the scores into a dict
    sentiment_dict = analyzer.polarity_scores(url) 
    if sentiment_dict['compound'] >= 0.05 : 
        category = ("Positive ")
    elif sentiment_dict['compound'] <= - 0.05 : 
        category = ("Negative ") 
    else : 
        category = ("Neutral ")
    print(category)
    
    if category == "Negative ":
        res='Hate Speech'
    else:
        res='Not Hate Speech'
    return jsonify({"sentiment":category,"verdict":res})
@app.route('/multi-class')
def category():
    url = request.args['url']

    # Print the output url.
    print(url)
    output=query_hate({
    "inputs": [str(url)],
    "keywords": ["LABEL_0", "LABEL_1", "LABEL_2", "LABEL_3"]})
    # print(output[0])
    result = {}
    if url:
        for data in output[0]:
            if data['label'] == "LABEL_0":
                result["ACCEPTABLE"] = round(data['score']*100, 2)
            elif data['label'] == "LABEL_1":
                result["INAPPROPRIATE"] = round(data['score']*100, 2)
            elif data['label'] == "LABEL_2":
                result["OFFENSIVE"] = round(data['score']*100, 2)
            elif data['label'] == "LABEL_3":
                result["VIOLENT"] = round(data['score']*100, 2)

        labels = list(result.keys())
        values = list(result.values())


    data = {"Target":list(result.keys()) , "Value": list(result.values())}
    df = pd.DataFrame(data)
    
    sns.barplot(x="Target" , y="Value", data=df, palette="Set2")
    plt.title("Hate Speech Params Detection present in Article")

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")
    plt.savefig('hate.png')

    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format="png")
    # buf.seek(0)
    # base64_string = base64.b64encode(buf.read()).decode("utf-8")

    # print(base64_string)
    # return base64_string

    return send_file("./hate.png", mimetype='image/png')


    # return jsonify({"result":result})

           
@app.route('/authenticity')
def auth():
    url = request.args['url']
    lis = []
    df = pd.read_csv('blacklist.csv')
    for i in range(len(df)):
        lis.append(df.loc[i, "MBFC"])

    for l in lis:
        if(url.__contains__(l)):
            return {"authentic":False}

    return { "authentic": True }

@app.route('/bot-activity')
def botActivity():
    url = request.args['url']
    i=0
    usernames = []
    time = []
    finalusername = []
    for tweet in snstwitter.TwitterSearchScraper(url).get_items():
        usernames.append(tweet.user.username)
        time.append(tweet.date)
        if(i==150):
            break
        i+=1

    flag = False
    for i in range(len(time)-1):
        a = time[i]
        b = time[i+1]
        c = a-b
        if(c.seconds <= 60):            
            finalusername.append(usernames[i+1])

    print("username: ", finalusername)
    if(len(finalusername) > 3):
        flag = True
    return jsonify({"bots":list(set(finalusername)),"flag":flag})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
