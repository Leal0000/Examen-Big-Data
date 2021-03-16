#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd 


# # Extraemos los datos de la api oficial modificada para poder extraer todos los datos existentes

# In[65]:


df = pd.read_json("https://smartdrape.000webhostapp.com/smartdrape/index.php/Controlador_arduino/extraccion")


# # Lo verificamos

# In[66]:


df


# # Visualizamos el contenido de las columnas 

# In[67]:


df.info()


# # Ahora visualizaremos los datos mas irrelevantes del dataframe

# In[5]:


df.describe()


# # Ahora bien relacionaremos los datos del clima los cuales seran analizados.

# In[6]:


relation = df[['temperatura','humedad','lluvia']]


# In[7]:


relation


# In[8]:


df.columns


# # Importamos las librerias para las graficas 

# In[9]:


import numpy as np 
import seaborn as sns 
from matplotlib import pyplot as plt 
get_ipython().magic('matplotlib inline')


# # Ahora veremos la relacion de estos datos en cuanto a la relacion que estos tienen 

# In[50]:


sns.pairplot(relation, kind='reg')
plt.show()
plt.savefig('img_web_site/general.png', transparent=True)


# In[49]:


sns.lmplot(relation, kind='reg')
plt.show()
plt.savefig('img_web_site/general.png', transparent=True)


# In[11]:


sns.distplot(df.temperatura)


# In[40]:


sns.lmplot(x='temperatura', y='humedad', data=df)
plt.savefig('img_web_site/hum-temp.png', transparent=True)


# In[42]:


sns.lmplot(x='temperatura', y='lluvia', data=df)
plt.savefig('img_web_site/temp-lluvia.png', transparent=True)


# In[43]:


sns.lmplot(x='lluvia', y='humedad', data=df)
plt.savefig('img_web_site/hum-lluvia.png', transparent=True)


# In[46]:


datanew = df.corr()
sns.lmplot(x='temperatura', y='humedad', data=datanew)
plt.savefig('img_web_site/corr-hum-temp.png', transparent=True)


# In[ ]:





# # Podemos ver la correlacion 

# In[47]:


df.corr()


# In[16]:


df


# # Ahora debido a que tenemos datos con punto decimal los convertiremos en flotantes

# In[17]:


df = df.astype({"temperatura":'float',
                "humedad":'float',
                "lluvia":'float',
                "distancia":'float',
               })


# In[18]:


df


# In[24]:


fig = df
plt.savefig('saved_figure.png', transparent=True)


# In[25]:


ls 


# In[27]:


df


# In[28]:


img = sns.lmplot(x='lluvia', y='humedad', data=df)


# In[33]:


fig = img.figure()
plt.savefig('figures.png', transparent=True)


# In[32]:



fig = plt.figure()

 

x = np.arange(0, 10, 0.1)
y = np.tan(x)

 

fig.suptitle('Tangente', fontsize=20)
plt.xlabel('xlabel', fontsize=18)
plt.ylabel('ylabel', fontsize=16)

 

plt.plot(x, y)

 

plt.savefig('saved_figures.png', transparent=True)


# In[ ]:





# # Agregamos las librerias para acceder a los csv de S3 y lo exportamos a nuestro bucket.

# In[19]:


from io import StringIO  
import boto3

 

bucket = 'testutmjesusleal' 
csv_buffer = StringIO()
df.to_csv(csv_buffer)

 

s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'datos1_smartdrape.csv').put(Body=csv_buffer.getvalue())


# # Importamos las librerias necesarias

# In[60]:


import logging
import boto3
from botocore.exceptions import ClientError


# In[61]:


import boto3
s3 = boto3.resource('s3')


# # Visualizamos los buckets existentes

# In[62]:


for bucket in s3.buckets.all():
    print(bucket.name)


# In[56]:


ls


# # Enviamos la imagen a S3

# In[70]:


data = open('temp-lluvia.png', 'rb')
s3.Bucket('miprimerapaginaleal').put_object(Key='img/temp-lluvia.png', Body=data)


# In[ ]:




