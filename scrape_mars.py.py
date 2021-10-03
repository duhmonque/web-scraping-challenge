#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymongo')


# In[2]:


get_ipython().system('pip install splinter')


# In[3]:


get_ipython().system('pip install webdriver_manager')


# In[4]:


# import dependencies
from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pymongo


# In[5]:


# Set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


# URL of page to be scrapped
url = 'https://mars.nasa.gov/news/9051/nasas-mars-fleet-lies-low-with-sun-between-earth-and-red-planet/'
browser.visit(url)
# Retrieve page with the requests module
response = requests.get(url, verify=True)
print(response.text)


# In[ ]:


title = ""
content = ""


# In[15]:


#Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


for paragraph in soup.find_all("p"):
    content = content + paragraph.get_text() + "\n"
   


# In[17]:


title = soup.title.get_text()


# In[18]:


title


# In[ ]:





# In[ ]:





# In[ ]:





# In[42]:


url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

# Retrieve page with the requests module
response = requests.get(url, verify=True)
print(response.text)


# In[46]:


from PIL import Image
from io import BytesIO


# img = Image.open(BytesIO(response.content))
featured_image_url
soup = BeautifulSoup(response.text, 'html.parser')
for image in browser.find_by_tag('img'):
    
    u = image['src']
    
    if(u.startswith("http") and "featured" in u):
        r = requests.get(u)
        featured_image_url = u
        pil_img = Image.open(BytesIO(r.content))
        display(pil_img)
    


# In[54]:


from urllib import request
import ssl

url = 'https://space-facts.com/mars/'
context = ssl._create_unverified_context()
response = request.urlopen(url, context=context)
html = response.read()
df_list = pd.read_html(html)
df_list


# In[66]:


html_string = ""
table1 = df_list[0]
table2 = df_list[1]
table3 = df_list[2]
table1.to_html('table1.html')
table2.to_html('table2.html')
table3.to_html('table3.html')
# for df in table1:
#     df.to_html('table.html')


# In[77]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
# Retrieve page with the requests module
response = requests.get(url, verify=True)

toVisitList = []

for link in browser.find_by_tag('a'):
    if("enhanced" in link['href'] and  link['href'] not in toVisitList ):
        toVisitList.append(link['href'])
toVisitList

# https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg


# In[85]:


fullImages = []
fullTitles = []
for link in toVisitList:
    browser.visit(link)
    for l in  browser.find_by_tag('a'):
        if("full.jpg" in l['href']):
            fullImages.append(l['href'])
            imageStr = l['href']
            arr = imageStr.split("/")
            temp = arr[len(arr)-2].replace('_enhanced.tif', '')
            result = temp.replace("_", " ").title()
            fullTitles.append(result)
print(fullImages)
print(fullTitles)


# In[88]:


hemisphere_image_urls = []
for i in range(0, len(fullImages)):
    dic = {}
    dic["title"] = fullTitles[i]
    dic["image_url"] = fullImages[i]
    hemisphere_image_urls.append(dic)
print(hemisphere_image_urls)


# In[ ]:




