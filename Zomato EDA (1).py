#!/usr/bin/env python
# coding: utf-8

# # Zomato Exploaratory Data Analysis

# ### Importing Libraries

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('zomato.csv', encoding = 'latin-1')


# ## Getting information from data

# In[4]:


df.head()


# In[63]:


df.tail(5)


# In[ ]:





# In[64]:


df.shape


# In[66]:


df.size


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.describe()


# # In Data Analysis what all things we do
# 1. Missing values
# 2. Explore about the Numerical Variables
# 3. Explore about the Categorical Variables
# 4. Finding Relationship between features

# In[8]:


df.isnull().sum()


# In[9]:


df['Cuisines'] = df['Cuisines'].fillna(0)


# In[10]:


df_country = pd.read_excel('Country-Code.xlsx')
df_country.head()


# ## Merging 2 Dataset

# In[11]:


final_df = pd.merge(df,df_country,on='Country Code', how='left')
final_df.head(2)


# In[69]:


final_df.shape


# In[70]:


final_df.size


# In[71]:


final_df.info()


# In[72]:


final_df.describe()


# In[12]:


final_df.columns


# In[13]:


country_name = final_df.Country.value_counts().index


# In[14]:


country_val = final_df.Country.value_counts().values


# In[15]:


##pie chart top 5 country uses zomato
plt.pie(country_val[:3], labels = country_name[:3], autopct="%1.2f%%")
plt.show()


# **Obsearvation**
# 1. In India , Zomato have most of the orders and transaction
# 2. United State following India and is in 2nd place 

# In[16]:


final_df.columns


# In[17]:


rating = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[18]:


rating


# **Observation**
# 1. When rating is between 4.5 to 4.9  --> Excellent
# 2. When rating is between 4.0 to 4.4  --> very good
# 3. When rating is between 3.5 to 3.9  --> good
# 4. When rating is between 2.5 to 3.4  --> Average
# 5. When rating is between 1.8 to 2.4  --> Poor
# 6. 2148 people are not rated

# In[19]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x='Aggregate rating', y = 'Rating count', hue = 'Rating color', data = rating, palette= ['blue','red','orange','yellow','green','green'])
plt.xlabel('Aggregated Rating')
plt.ylabel('Rating Count')
plt.title('Rating by People')
plt.show()


# **Observation**
# 1. Not rated count is very high
# 2. Maximum number of rating between 2.4 to 3.4

# In[20]:


#count plot
sns.countplot(x='Rating color', data = rating, palette= ['blue','red','orange','yellow','green','green'] )


# In[21]:


rating.head()


# In[22]:


final_df[final_df['Rating color'] == 'White'].groupby('Country').size().reset_index()


# **Observation**
# 1. MAximum number of 0 rating are given from Indian customers
# 2. United Kingdom customers are given at least 1 ratinf

# In[23]:


final_df.groupby(['Country', 'Currency']).size().reset_index()


# In[24]:


final_df.groupby(['Country', 'Has Online delivery']).size().reset_index()


# In[25]:


final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()


# **Observation** 
# India and UAE only countries have online delivery.

# In[26]:


final_df[final_df['Has Table booking']=='Yes'].Country.value_counts()


# **Observaation** 
# India have more order in table booking than any other country

# In[27]:


city_name = final_df.City.value_counts().index


# In[28]:


city_val = final_df.City.value_counts().values


# In[29]:


plt.pie(city_val[:5], labels = city_name[:5], autopct = '%1.2f%%')
plt.show()


# **Observation**
# 1. Delhi has more order than any order than city.
# 2. Gurgaon and Noida are close to each other.

# In[40]:


n =sns.barplot('Country', 'Price range', data = final_df)
plt.xlabel('Country')
plt.ylabel('Price range')
n = plt.xticks(rotation = 90)


# **Observation**
# 1. In Singapore, the price range is higher than any other country
# 2. Qatar and South Africa following singapore they are in 2nd and 3rd position

# ## Thank You !
