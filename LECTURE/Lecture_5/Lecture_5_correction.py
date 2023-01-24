#!/usr/bin/env python
# coding: utf-8

# # Web scrapping

# ## Scrapping directly a document

# In[1]:


#import request library
import requests
print(requests.__version__)


# In[6]:


# Create a request
resp = requests.get('https://www.python.org/static/img/python-logo.png')


# In[9]:


#print the answer
# print(resp.content)
with open(r'D:\KBTU\2022-2023\Python Course\Course_beginners\Lecture\Lecture_5\image_temp.png', 'wb') as file:
    file.write(resp.content)


# In[11]:


#YOUR TURN
# Choose a website and print its html in your console !
#Just request the website
#10 minutes
resp = requests.get("https://www.google.com")
print(resp.content)


# In[12]:


#Create a headers to get better result
#use the header from the "inspect" tool
#print the answer
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get("https://www.google.com", headers = headers)
print(resp.content)


# In[15]:


#YOUR TURN
#identify you headers of your web browser and use them to access to a website
#5 minutes
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://finance.yahoo.com/', headers = headers)
print(resp)


# In[20]:


#Let's try with yahoo finance website  
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633297421&period2=1664833421&interval=1d&events=history&includeAdjustedClose=true', 
                    headers = headers)
print(resp.content)


# In[ ]:


#YOUR TURN
#Try to get your own stock csv
#Go to yahoo finance => your company historical data => Open inspect tool =< Download data => copy url of request to do it with python
#10 minutes


# In[25]:


#Finding the time period
#1 year period : from 1633297421 to 1664833421
print((1633297421 - 1664833421)/3600/24/365)
#period is in second
#When is the beginning ?
#04/10/2022 = 1664833421
print(1664833421/3600/24/365)
#beginning is 52.8 years ago => 01/01/1970


# In[41]:


#Automatize date choice
import datetime
origin_date = datetime.datetime(year = 1970, month = 1, day = 1)
begin_date = datetime.datetime(year = 2022, month = 10, day = 4)
difference = begin_date-origin_date
print(difference.total_seconds())


# In[50]:


#Choose your own dates
begin_date = datetime.datetime(year = 2020, month = 9, day = 4)
begin_seconds = begin_date-origin_date
end_date = datetime.datetime(year = 2022, month = 10, day = 4)
end_seconds = end_date-origin_date

parameters = {'period1' : str(int(begin_seconds.total_seconds())), 'period2' : str(int(end_seconds.total_seconds())), 'interval' : '1d', 'events': 'history',
              'includeAdjustedClose': 'true'}

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT', params = parameters ,
                    headers = headers)
print(resp.content)


# In[ ]:


#YOUR TURN
#get your csv file from practice 1 with a python resquest with another date
#10 minutes


# # Scrapping a page

# In[52]:


#Get the html file with a query on google news
url = 'https://news.google.com/search?q=tesla&hl=en-US&gl=US&ceid=US%3Aen'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0', 'Accept-Language' : 'en-GB,en;q=0.5'}

resp = requests.get(url, headers = headers)
print(resp.text)


# In[54]:


# Extracting news data on company with BeautifulSoup
from bs4 import BeautifulSoup
import requests

#Use the url found with private browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0', 'Accept-Language' : 'en-GB,en;q=0.5'}
page = requests.get('https://news.google.com/search?q=tesla&hl=en-US&gl=US&ceid=US%3Aen',
                    headers = headers)
print(page.content)
bs = BeautifulSoup(page.content)


# In[71]:


#Display info 
#Docs at : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# print(bs.prettify())
print(bs.find_all('h3')[10].string)


# In[72]:


#YOUR TURN
#Identify all url of the news about your stock
# 10 minutes
#Request the news page of your company
#Make a beautifulsoup object from it
#Get all h3 title text of them with a loop

for i in bs.find_all('h3'):
    print(i.string)


# # Browser-based scrapping : Selenium

# In[73]:


#import the package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# In[74]:


#Download geckodriver from here : https://github.com/mozilla/geckodriver/releases
#Unzip it
#Add the path to geckodriver folder to the system path


# In[76]:


#Create your browser
browser = webdriver.Firefox()  
#open the required page
browser.get("https://www.python.org")
browser.maximize_window()


# In[77]:


#print some information
print(browser.title)


# In[78]:


#Fin the research bar and write in it
search_bar = browser.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")


# In[79]:


#Run the research
search_bar.send_keys(Keys.RETURN)


# In[ ]:




