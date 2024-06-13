#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("supermarket_sales - Sheet1.csv")
df.info
print(df.head())


# In[7]:


# check for missing values
df.dropna(inplace=True)

df.describe()


# In[8]:


# Sales over time

sales_over_time = df.groupby('Date')['Total'].sum()


#Plot sales over time 

plt.figure(figsize=(10, 6))
sales_over_time.plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()


# In[9]:


# Product Category Performance

category_sales = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[11]:


# Sales by Gender

product_sales = df.groupby('Gender')['Total'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[12]:


# Sales by City

city_sales = df.groupby('City')['Total'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x= city_sales.index, y=city_sales.values)
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# In[13]:


# Sales by Payment

payment_type = df.groupby('Payment')['Total'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=payment_type.index, y=payment_type.values)
plt.title("Sales by Payment Type")
plt.xlabel("Payment Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




