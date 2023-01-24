#!/usr/bin/env python
# coding: utf-8

# # LECTURE 6

# # Correction of the practice

# In[ ]:


import requests

url = 'https://query1.finance.yahoo.com/v7/finance/download/APP?period1=1633911045&period2=1665447045&interval=1d&events=history&includeAdjustedClose=true'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get(url, headers = headers)

print(resp.content)
# print(resp.request.headers)


# In[ ]:


import pandas as pd
import io
df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
print(df)


# In[ ]:


df = pd.read_csv(url)
print(df)


# In[ ]:


import requests
l = ['TSLA', 'AAPL', 'MSFT']
for i in l:
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+i+'?period1=1633911045&period2=1665447045&interval=1d&events=history&includeAdjustedClose=true'
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
    resp = requests.get(url, headers = headers)

    df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
    print(df)


# # LECTURE

# # Reminder => make a request

# In[ ]:


#YOUR TURN: Make a request to any website (except websites with login requiered) and print the html code
#10 minutes => 16:32
import requests
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.google.com', headers = headers)
print(resp.content)


# # BeautifulSoup and Html

# ## Reminder

# In[ ]:


#Get the html file of a website
import requests
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
print(resp.content)


# In[ ]:


#Install and import beautiful soup
#pip install bs4
from bs4 import BeautifulSoup


# In[ ]:


#Make the soup !
soup = BeautifulSoup(resp.content)
print(soup.prettify())


# In[ ]:


#YOUR TURN
#Make a soup of athe weather website (link on teams)
#16:42


# # Using the soup

# ## Some useful functions

# In[51]:


#Getting a html file in my files
from bs4 import BeautifulSoup
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_6\html_example.html", 'r') as file:
    a = file.read()
    
soup = BeautifulSoup(a)
# print(content)


# In[5]:


# prettify
print(soup.prettify())


# In[14]:


# Going trough tags
print(soup.aside.ul)


# In[15]:


#YOUR TURN print the following tag <div class = 'header-inner'
#16:55

import requests
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')

print(soup.body.div.div.div.div)


# In[21]:


# iteration on children of a tag:
for child in soup.body.header.div.children:
    print(child)


# In[22]:


#On all descendant
for desc in soup.body.header.div.descendants:
    print(desc)


# In[28]:


# Get the content of a tag
print(soup.body.header.contents)


# In[30]:


#Get the string of a tag (only if no more children)
print(soup.body.header.h1.string)


# In[38]:


#Finding all
print(soup.find_all('li'))


# In[46]:


# more about find_all
# filtering with id
print(soup.find_all('a', id = 'the_link'))


# In[47]:


#filtering with class
print(soup.find_all('i', class_ = 'fab fa-facebook'))


# In[50]:


#filtering with several attribute
attrs = {'id' : 'the_link', 'class' : 'fab fa-facebook'}
print(soup.find_all('a', attrs))


# In[53]:


# Getting info of the tag
print(soup.find_all('a', attrs)[0]['href'])


# In[59]:


#find_all of find _al
print(soup.find_all('div', class_ = 'social')[0].find_all('i', class_ = 'fab fa-facebook'))


# In[67]:


#YOUR TURN : Get the current temperature and today air quality in the weather website
#15 minutes
#=> 17:40
import requests
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')


# In[73]:


print(soup.find('div', class_ = 'cur-con-weather-card__body').find('div', class_ = "temp").text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




