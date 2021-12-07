#!/usr/bin/env python
# coding: utf-8

# In[52]:


# !pip install pyttsx3
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia


# In[2]:


#listen to our microphone and return the audio as text using google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listening')
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"


# In[3]:


transform()


# In[4]:


def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


# In[17]:


speaking('hello world')
# speaking('Hallo Welt')


# In[9]:


engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)


# In[45]:


id ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello World')
engine.runAndWait()


# In[24]:


#returns the weekday name
def query_day():
    day = datetime.date.today()
    #print(day)
    weekday = day.weekday()
    #print(weekday)
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass


# In[49]:


query_day()


# In[72]:


#returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[0:2]} o'clock and {time[3:5]} minutes")


# In[73]:


query_time()


# In[48]:


#Intro greeting at startup
def whatsup():
    speaking('''Hi, I am David.
    How may I help you?
    ''')


# In[46]:


whatsup()


# In[66]:


#the heart of our assistant. Takes queries and returns answers
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()
        
        if 'start youtube' in q:
            speaking('starting youtube. Just a second.')
            webbrowser.open('https://www.youtube.com')
            continue
            
        elif 'start webbrowser' in q:
            speaking('opening browser')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'what day is it' in q:
            query_day()
            continue
            
        elif 'what time is it' in q:
            query_time()
            continue
            
        elif "shut down" in q:
            speaking('ok I am shutting down')
            break
        
        elif "from wikipedia" in q:
            speaking('checking wikipedia')
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue
        
        elif "your name" in q:
            speaking('I am David. Your VA')
            continue
            
        elif "search web" in q:
            pywhatkit.search(q)
            speaking('that is what I found')
            continue
            
        elif "play" in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
            
        elif "joke" in q:
            speaking(pyjokes.get_joke())
            continue
            
        elif "stock price" in q:
            search  = q.split("of")[-1].strip()
            lookup = {'apple':'AAPL',
                     'amazon':'AMZN',
                     'google':"GOOGL"}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speaking(f'sorry I have no data for {search}')
                continue


# In[69]:


querying()


# In[ ]:




