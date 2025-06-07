#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


URL = 'https://www.quikr.com/cars/used+Maruti-Suzuki+Swift-Dzire+cars+all-india+z1399vbd'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

res = requests.get(URL, headers=headers)


# In[3]:


res.status_code


# In[4]:


# res.text # Total page content


# In[5]:


len(res.text) # No. of characters in page


# In[6]:


content = res.text
content[:1000] # 1000 characters


# In[7]:


# Creating an html page in destination folder
with open('quikrSuzuki.html', 'w', encoding="utf-8") as f:
    f.write(content)


# In[8]:


from bs4 import BeautifulSoup


# In[9]:


soup = BeautifulSoup(content, 'html.parser')


# In[10]:


div_tags = soup.find_all('div')


# In[11]:


len(div_tags)  # No.of div tags available in webpage


# In[58]:


carname_div = soup.find_all('div', class_='car-info__footer')
len(carname_div)


# In[61]:


carname_div = soup.find_all("div", {"class": "car-info__footer"})
carname_div = [el.findChildren()[0] for el in carname_div]  # Getting first child of each div_cl
carname_div[:5]


# In[63]:


carname_div[0].text


# In[64]:


car_names = []

for car in div_cl:
    car_names.append(car.text)
    
car_names


# In[65]:


feature_div = soup.find_all('div', {
    'class' : 'prime-features'
})

len(feature_div)


# In[67]:


feature_div[0].text


# In[68]:


features = []

for feature in feature_div:
    features.append(feature.text)
    
features


# In[70]:


cls = 'price'
price_div = soup.find_all('div', {
    'class' : cls
})

len(price_div)


# In[71]:


prices = []

for price in price_div:
    prices.append(price.text)
    
prices


# In[72]:


# Converting data into a DataFrame
import pandas as pd


# In[73]:


cars_dict = {
    'Name' : car_names,
    'Features' : features,
    'Price' : prices
}


# In[74]:


cars_df = pd.DataFrame(cars_dict)


# In[75]:


cars_df


# In[76]:


# Converting DataFrame into a csv file
cars_df.to_csv('QuikrSuzukiCars.csv') # QuikrSuzukiCars.csv file will be created in destination folder


# In[ ]:




