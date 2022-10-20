#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df2015 = pd.read_csv("2015.csv")
df2016 = pd.read_csv("2016.csv")
df2017 = pd.read_csv("2017.csv")
df2018 = pd.read_csv("2018.csv")
df2019 = pd.read_csv("2019.csv")


# In[2]:


df2015.head()


# In[3]:


df2015.info()


# In[4]:


df2016.head()


# In[5]:


df2016.info()


# In[6]:


df2017.head()


# In[7]:


df2017.info()


# In[8]:


df2018.head()


# In[9]:


df2018.info()


# In[10]:


df2018['Perceptions of corruption'] = df2018['Perceptions of corruption'].fillna(0)


# In[11]:


df2018.info()


# In[12]:


df2019.head()


# In[13]:


df2019.info()


# In[14]:


df2015.duplicated().sum(), 
df2016.duplicated().sum(), 
df2017.duplicated().sum(), 
df2018.duplicated().sum(), 
df2019.duplicated().sum()


# In[15]:


df2015.isnull().sum()


# In[16]:


df2016.isnull().sum()


# In[17]:


df2017.isnull().sum()


# In[18]:


df2018.isnull().sum()


# In[19]:


df2019.isnull().sum()


# In[20]:


print('2015.csv contains:')
print(df2015.columns)
print('2016.csv contains:')
print(df2016.columns)
print('2017.csv contains:')
print(df2017.columns)
print('2018.csv contains:')
print(df2018.columns)
print('2019.csv contains:')
print(df2019.columns)


# In[21]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
df2015 = pd.read_csv("2015.csv")
data = dict(
type = 'choropleth',
colorscale = 'RdYlBu',
marker_line_width=1,
locations = df2015['Country'],
locationmode = "country names",
z = df2015['Happiness Score'],
text = df2015['Country'],
colorbar = {'title' : 'Happiness score scale'},
)
layout = dict(title = 'World happiness map for 2015:',
geo = dict(projection = {'type':'mercator'}, showocean = False, showlakes = True, showrivers = True, )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[22]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
df2016 = pd.read_csv("2016.csv")
data = dict(
type = 'choropleth',
colorscale = 'RdYlBu',
marker_line_width=1,
locations = df2016['Country'],
locationmode = "country names",
z = df2016['Happiness Score'],
text = df2016['Country'],
colorbar = {'title' : 'Happiness score scale'},
)
layout = dict(title = 'World happiness map for 2016:',
geo = dict(projection = {'type':'mercator'}, showocean = False, showlakes = True, showrivers = True, )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[23]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
df2017 = pd.read_csv("2017.csv")
data = dict(
type = 'choropleth',
colorscale = 'RdYlBu',
marker_line_width=1,
locations = df2017['Country'],
locationmode = "country names",
z = df2017['Happiness.Score'],
text = df2017['Country'],
colorbar = {'title' : 'Happiness score scale'},  
)
layout = dict(title = 'World happiness map for 2017:',
geo = dict(projection = {'type':'mercator'}, showocean = False, showlakes = True, showrivers = True, )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[24]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
df2018 = pd.read_csv("2018.csv")
data = dict(
type = 'choropleth',
colorscale = 'RdYlBu',
marker_line_width=1,
locations = df2018['Country or region'],
locationmode = "country names",
z = df2018['Score'],
text = df2018['Country or region'],
colorbar = {'title' : 'Happiness score scale'},
)
layout = dict(title = 'World happiness map for 2018:',
geo = dict(projection = {'type':'mercator'}, showocean = False, showlakes = True, showrivers = True, )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[25]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
df2019 = pd.read_csv("2019.csv")
data = dict(
type = 'choropleth',
colorscale = 'RdYlBu',
marker_line_width=1,
locations = df2019['Country or region'],
locationmode = "country names",
z = df2019['Score'],
text = df2019['Country or region'],
colorbar = {'title' : 'Happiness score scale'},
)
layout = dict(title = 'World happiness map for 2019:',
geo = dict(projection = {'type':'mercator'}, showocean = False, showlakes = True, showrivers = True, )
)
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2015 = pd.read_csv("2015.csv")
corrMatrix2015 = df2015.corr()
print(corrMatrix2015)
sns.heatmap(corrMatrix2015,annot=True)
plt.title ('Correlation heatmap')
plt.title('Correlation coefficients for 2015 data:', fontsize=14)


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2015 = pd.read_csv("2015.csv")
sns.pairplot(df2015,kind = 'reg', vars =['Happiness Score', 'Economy (GDP per Capita)','Family','Health (Life Expectancy)',
'Freedom','Generosity'])
print('Correlation matrix for 2015 data:')


# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2016 = pd.read_csv("2016.csv")
corrMatrix2016 = df2016.corr()
print(corrMatrix2016)
sns.heatmap(corrMatrix2016,annot=True)
plt.title ('Correlation heatmap')
plt.title('Correlation coefficients for 2016 data:', fontsize=14)


# In[29]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2016 = pd.read_csv("2016.csv")
sns.pairplot(df2016,kind = 'reg', vars =['Happiness Score', 'Economy (GDP per Capita)','Family','Health (Life Expectancy)',
'Freedom','Generosity'])
print('Correlation matrix for 2016 data:')


# In[30]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2017 = pd.read_csv("2017.csv")
corrMatrix2017 = df2017.corr()
print(corrMatrix2017)
sns.heatmap(corrMatrix2017,annot=True)
plt.title ('Correlation heatmap')
plt.title('Correlation coefficients for 2017 data:', fontsize=14)


# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2017 = pd.read_csv("2017.csv")
sns.pairplot(df2017,kind = 'reg', vars =['Happiness.Score', 'Economy..GDP.per.Capita.','Family','Health..Life.Expectancy.',
'Freedom','Generosity'])
print('Correlation matrix for 2017 data:')


# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2018 = pd.read_csv("2018.csv")
corrMatrix2018 = df2018.corr()
print(corrMatrix2018)
sns.heatmap(corrMatrix2018,annot=True)
plt.title ('Correlation heatmap')
plt.title('Correlation coefficients for 2018 data:', fontsize=14)


# In[33]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2018 = pd.read_csv("2018.csv")
sns.pairplot(df2018,kind = 'reg', vars =['Score','GDP per capita','Social support','Healthy life expectancy',
'Freedom to make life choices','Generosity'])
print('Correlation matrix for 2018 data:')


# In[34]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2019 = pd.read_csv("2019.csv")
corrMatrix2019 = df2019.corr()
print(corrMatrix2019)
sns.heatmap(corrMatrix2019,annot=True)
plt.title ('Correlation heatmap')
plt.title('Correlation coefficients for 2019 data:', fontsize=14)


# In[35]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2019 = pd.read_csv("2019.csv")
sns.pairplot(df2019,kind = 'reg', vars =['Score','GDP per capita','Social support','Healthy life expectancy',
'Freedom to make life choices','Generosity'])
print('Correlation matrix for 2019 data:')


# In[36]:


from plotly.offline import iplot
import pandas as pd 
year2015 = pd.read_csv('2015.csv')
year2016 = pd.read_csv('2016.csv')
year2017 = pd.read_csv('2017.csv')
year2018 = pd.read_csv('2018.csv')
year2019 = pd.read_csv('2019.csv')
df2015 = year2015.iloc[:20,:]
df2016 = year2016.iloc[:20,:]
df2017 = year2017.iloc[:20,:]
df2018 = year2018.iloc[:20,:]
df2019 = year2019.iloc[:20,:]
import plotly.graph_objs as go
trace1 =go.Scatter(
x = df2015['Country'],
y = df2015['Happiness Score'],
mode = "markers",
name = "2015",
marker = dict(color = 'lightcoral'),
text= df2015.Country)
trace2 =go.Scatter(
x = df2015['Country'],
y = df2016['Happiness Score'],
mode = "markers",
name = "2016",
marker = dict(color = 'limegreen'),
text= df2016.Country)
trace3 =go.Scatter(
x = df2015['Country'],
y = df2017['Happiness.Score'],
mode = "markers",
name = "2017",
marker = dict(color = 'royalblue'),
text= df2017.Country)
trace4 =go.Scatter(
x = df2015['Country'],
y = df2018['Score'],
mode = "markers",
name = "2018",
marker = dict(color = 'mediumorchid'),
text= df2017.Country)
trace5 =go.Scatter(
x = df2015['Country'],
y = df2019['Score'],
mode = "markers",
name = "2019",
marker = dict(color = 'darkgoldenrod'),
text= df2017.Country)
data = [trace1, trace2, trace3, trace4, trace5]
layout = dict(title = 'Happiness rates changing for 20 highest ranking countries from 2015 to 2019:',
xaxis= dict(title= 'Country',ticklen= 5,zeroline= False),
yaxis= dict(title= 'Happiness Rate',ticklen= 5,zeroline= False),
hovermode="x unified"
)
fig = dict(data = data, layout = layout)
iplot(fig)


# In[37]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df2015 = pd.read_csv("2015.csv")
df2016 = pd.read_csv("2016.csv")
df2017 = pd.read_csv("2017.csv")
df2018 = pd.read_csv("2018.csv")
df2019 = pd.read_csv("2019.csv")
plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Happiness Score'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Happiness Score'],color='turquoise', label='2016')
sns.kdeplot(df2017['Happiness.Score'],color='seagreen', label='2017')
sns.kdeplot(df2018['Score'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Score'],color='tomato', label='2019')
plt.title('Happiness rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[38]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Economy (GDP per Capita)'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Economy (GDP per Capita)'],color='turquoise', label='2016')
sns.kdeplot(df2017['Economy..GDP.per.Capita.'],color='seagreen', label='2017')
sns.kdeplot(df2018['GDP per capita'],color='blueviolet', label='2018')
sns.kdeplot(df2019['GDP per capita'],color='tomato', label='2019')
plt.title('Economy - GDP per capita rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[39]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Family'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Family'],color='turquoise', label='2016')
sns.kdeplot(df2017['Family'],color='seagreen', label='2017')
sns.kdeplot(df2018['Social support'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Social support'],color='tomato', label='2019')
plt.title('Family - social support rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[40]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Health (Life Expectancy)'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Health (Life Expectancy)'],color='turquoise', label='2016')
sns.kdeplot(df2017['Health..Life.Expectancy.'],color='seagreen', label='2017')
sns.kdeplot(df2018['Healthy life expectancy'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Healthy life expectancy'],color='tomato', label='2019')
plt.title('Health - life expectancy rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[41]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Freedom'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Freedom'],color='turquoise', label='2016')
sns.kdeplot(df2017['Freedom'],color='seagreen', label='2017')
sns.kdeplot(df2018['Freedom to make life choices'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Freedom to make life choices'],color='tomato', label='2019')
plt.title('Freedom rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[42]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Trust (Government Corruption)'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Trust (Government Corruption)'],color='turquoise', label='2016')
sns.kdeplot(df2017['Trust..Government.Corruption.'],color='seagreen', label='2017')
sns.kdeplot(df2018['Perceptions of corruption'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Perceptions of corruption'],color='tomato', label='2019')
plt.title('Trust - corruption rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[43]:


plt.figure(figsize=(10,5))
sns.kdeplot(df2015['Generosity'],color='goldenrod', label='2015')
sns.kdeplot(df2016['Generosity'],color='turquoise', label='2016')
sns.kdeplot(df2017['Generosity'],color='seagreen', label='2017')
sns.kdeplot(df2018['Generosity'],color='blueviolet', label='2018')
sns.kdeplot(df2019['Generosity'],color='tomato', label='2019')
plt.title('Generosity rates changing from 2015 to 2019:',size=20)
plt.legend()
plt.show()


# In[44]:


import plotly.graph_objs as go
from plotly.offline import iplot
import pandas as pd
year2015 = pd.read_csv('2015.csv')
df = year2015.iloc[:50,:]
trace1 = go.Scatter(x = df['Country'],
y = df['Economy (GDP per Capita)'],
mode = "lines+markers",
name = "Economy",
marker = dict(color = 'palevioletred'),
text= df.Country)
trace2 = go.Scatter(x = df['Country'],
y = df['Freedom'],
mode = "lines+markers",
name = "Freedom",
marker = dict(color = 'limegreen'),
text= df.Country)
trace3 = go.Scatter(x = df['Country'],
y = df['Trust (Government Corruption)'],
mode = "lines+markers",
name = "Trust",
marker = dict(color = 'deepskyblue'),
text= df.Country)
trace4 = go.Scatter(x = df['Country'],
y = df['Dystopia Residual'],
mode = "lines+markers",
name = "Dystopia Residual",
marker = dict(color = 'black'),
text= df.Country)
data = [trace1, trace2, trace3, trace4]
layout = dict(title = 'Comparison of economy, freedom and trust rates with dystopia residual values for 2015:',
xaxis= dict(title= 'Countries',ticklen= 5,zeroline= False),
hovermode="x unified")
fig = dict(data = data, layout = layout)
iplot(fig)


# In[45]:


year2016 = pd.read_csv('2016.csv')
df = year2016.iloc[:50,:]
trace1 = go.Scatter(x = df['Country'],
y = df['Economy (GDP per Capita)'],
mode = "lines+markers",
name = "Economy",
marker = dict(color = 'palevioletred'),
text= df.Country)
trace2 = go.Scatter(x = df['Country'],
y = df['Freedom'],
mode = "lines+markers",
name = "Freedom",
marker = dict(color = 'limegreen'),
text= df.Country)
trace3 = go.Scatter(x = df['Country'],
y = df['Trust (Government Corruption)'],
mode = "lines+markers",
name = "Trust",
marker = dict(color = 'deepskyblue'),
text= df.Country)
trace4 = go.Scatter(x = df['Country'],
y = df['Dystopia Residual'],
mode = "lines+markers",
name = "Dystopia Residual",
marker = dict(color = 'black'),
text= df.Country)
data = [trace1, trace2, trace3, trace4]
layout = dict(title = 'Comparison of economy, freedom and trust rates with dystopia residual values for 2016:',
xaxis= dict(title= 'Countries',ticklen= 5,zeroline= False),
hovermode="x unified")
fig = dict(data = data, layout = layout)
iplot(fig)


# In[46]:


year2017 = pd.read_csv('2017.csv')
df = year2017.iloc[:50,:]
trace1 = go.Scatter(x = df['Country'],
y = df['Economy..GDP.per.Capita.'],
mode = "lines+markers",
name = "Economy",
marker = dict(color = 'palevioletred'),
text= df.Country)
trace2 = go.Scatter(x = df['Country'],
y = df['Freedom'],
mode = "lines+markers",
name = "Freedom",
marker = dict(color = 'limegreen'),
text= df.Country)
trace3 = go.Scatter(x = df['Country'],
y = df['Trust..Government.Corruption.'],
mode = "lines+markers",
name = "Trust",
marker = dict(color = 'deepskyblue'),
text= df.Country)
trace4 = go.Scatter(x = df['Country'],
y = df['Dystopia.Residual'],
mode = "lines+markers",
name = "Dystopia Residual",
marker = dict(color = 'black'),
text= df.Country)
data = [trace1, trace2, trace3, trace4]
layout = dict(title = 'Comparison of economy, freedom and trust rates with dystopia residual values for 2017:',
xaxis= dict(title= 'Countries',ticklen= 5,zeroline= False),
hovermode="x unified")
fig = dict(data = data, layout = layout)
iplot(fig)


# In[47]:


df=pd.read_csv("2019.csv")
df.head()
original=df.copy()
def highlight_max(s):    
    is_max = s == s.max()
    return ['background-color: greenyellow' if v else '' for v in is_max]
df.style.apply(highlight_max, subset=['Score','GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption'])


# In[48]:


df.shape


# In[49]:


print('Max:',df['Score'].max())
print('Min:',df['Score'].min())
add=df['Score'].max()-df['Score'].min()
grp=round(add/3,3)
print('Range difference:',(grp))


# In[50]:


low=df['Score'].min()+grp
mid=low+grp
print('Upper bound of low group:',low)
print('Upper bound of mid group:',mid)
print('Upper bound of high group:',df['Score'].max())


# In[51]:


cat=[]
for i in df.Score:
    if(i>0 and i<low):
        cat.append('Low')
    elif(i>low and i<mid):
         cat.append('Mid')
    else:
         cat.append('High')
df['Category']=cat  
color = (df.Category == 'High' ).map({True: 'background-color: greenyellow',False:'background-color: lightpink'})
df.style.apply(lambda s: color)


# In[52]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df2019 = pd.read_csv('2019.csv')
fig, axes = plt.subplots(nrows=2, ncols=2,constrained_layout=True,figsize=(12,8))
sns.barplot(x='GDP per capita',y='Country or region',data=df2019.nlargest(10,'GDP per capita'),ax=axes[0,0],palette="summer")
sns.barplot(x='Social support' ,y='Country or region',data=df2019.nlargest(10,'Social support'),ax=axes[0,1],palette="Wistia")
sns.barplot(x='Healthy life expectancy' ,y='Country or region',data=df2019.nlargest(10,'Healthy life expectancy'),ax=axes[1,0],palette='Wistia')
sns.barplot(x='Freedom to make life choices' ,y='Country or region',data=df2019.nlargest(10,'Freedom to make life choices'),ax=axes[1,1],palette='summer')
fig, axes = plt.subplots(nrows=1, ncols=2,constrained_layout=True,figsize=(10,4))
sns.barplot(x='Generosity' ,y='Country or region',data=df2019.nlargest(10,'Generosity'),ax=axes[0],palette='summer')
sns.barplot(x='Perceptions of corruption' ,y='Country or region',data=df2019.nlargest(10,'Perceptions of corruption'),ax=axes[1],palette='Wistia')


# In[53]:


import pandas as pd
df20166 = pd.read_csv("20166.csv")
df20166.head(5)


# In[54]:


from sklearn import datasets
region=df20166.groupby(['Region']).Score.mean()
region_df=pd.DataFrame(data=region)
reg=region_df.sort_values(by='Score',ascending=False,axis=0)
reg


# In[55]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
plt.title('Happiness rates across different regions of the world:')
sns.barplot(x='Score',y=reg.index,data=reg,palette='coolwarm')


# In[56]:


trust=df20166.groupby(['Region'])['Trust (Government Corruption)'].mean()
trust_df=pd.DataFrame(data=trust)
tru=trust_df.sort_values(by='Trust (Government Corruption)',ascending=False,axis=0)
tru


# In[57]:


plt.figure(figsize=(10,7))
plt.title('Satisfaction with governments across different regions of the world:')
sns.barplot(x='Trust (Government Corruption)',y=tru.index,data=tru,palette='coolwarm')


# In[58]:


gdpc=df20166.groupby(['Region'])['Economy (GDP per Capita)'].mean()
gdpc_df=pd.DataFrame(data=gdpc)
gdp=gdpc_df.sort_values(by='Economy (GDP per Capita)',ascending=False,axis=0)
gdp


# In[59]:


plt.figure(figsize=(10,7))
plt.title('Economy (GDP per capita) across different regions of the world:')
sns.barplot(x='Economy (GDP per Capita)',y=gdp.index,data=gdp,palette='coolwarm')


# In[60]:


import pandas as pd
df=pd.read_csv("2019.csv")
original=df.copy()
original=original.drop(['Country or region','Overall rank'],axis=1)
df.head()


# In[61]:


from sklearn.preprocessing import normalize
data_scaled = normalize(original)
data_scaled = pd.DataFrame(data_scaled, columns=original.columns)
datasc=data_scaled.copy()
data_scaled.head()


# In[62]:


import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 8))  
plt.title("Dendrograms (will help in deciding the number of clusters):")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))


# In[63]:


plt.figure(figsize=(10, 7))  
plt.title("Dendrograms:")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.axhline(y=0.5, color='r', linestyle='--')


# In[64]:


from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  
cluster.fit_predict(data_scaled)


# In[65]:


plt.figure(figsize=(6, 5))  
plt.scatter(data_scaled['GDP per capita'], data_scaled['Perceptions of corruption'], c=cluster.labels_) 
plt.xlabel('GDP Per Capita')
plt.ylabel('Perceptions Of Corruption')
plt.colorbar()


# In[66]:


X = datasc[["Social support","Healthy life expectancy"]]
plt.scatter(X["Social support"],X["Healthy life expectancy"],c='deepskyblue')
plt.show()


# In[67]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(X['Social support'], X['Healthy life expectancy'], c= kmeans.labels_.astype(float), alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
plt.show()


# In[68]:


import pandas as pd
df2019 = pd.read_csv("2019.csv")
df2019.loc[df2019['Country or region']=='India']


# In[69]:


d= df2019[(df2019['Country or region'].isin(['India','Canada','United Kingdom', 'United States']))]
d


# In[70]:


import matplotlib.pyplot as plt
ax = d.plot(y="Social support", x="Country or region", kind="bar",color='sandybrown')
d.plot(y="GDP per capita", x="Country or region", kind="bar", ax=ax, color="cornflowerblue")
d.plot(y="Healthy life expectancy", x="Country or region", kind="bar", ax=ax, color="limegreen")
plt.show()


# In[71]:


ax = d.plot(y="Freedom to make life choices", x="Country or region", kind="bar",color='sandybrown')
d.plot(y="Generosity", x="Country or region", kind="bar", ax=ax, color="cornflowerblue",)
d.plot(y="Perceptions of corruption", x="Country or region", kind="bar", ax=ax, color="limegreen",)
plt.show()


# In[72]:


df2015 = pd.read_csv("2015.csv")
df2016 = pd.read_csv("2016.csv")
df2017 = pd.read_csv("2017.csv")
df2018 = pd.read_csv("2018.csv")
df2019 = pd.read_csv("2019.csv")
df2018['Year']='2018'
df2019['Year']='2019'
df2015['Year']='2015'
df2016['Year']='2016'
df2017['Year']='2017'
df2019.rename(columns={'Country or region':'Country'},inplace=True)
data1=df2019.filter(['Country','GDP per capita','Year'],axis=1)
df2015.rename(columns={'Economy (GDP per Capita)':'GDP per capita'},inplace=True)
data2=df2015.filter(['Country','GDP per capita',"Year"],axis=1)
df2016.rename(columns={'Economy (GDP per Capita)':'GDP per capita'},inplace=True)
data3=df2016.filter(['Country','GDP per capita',"Year"],axis=1)
df2017.rename(columns={'Economy..GDP.per.Capita.':'GDP per capita'},inplace=True)
data4=df2017.filter(['Country','GDP per capita','Year'],axis=1)
df2018.rename(columns={'Country or region':'Country'},inplace=True)
data5=df2018.filter(['Country','GDP per capita',"Year"],axis=1)
data2=data2.append([data3,data4,data5,data1])
d


# In[73]:


import seaborn as sns
plt.figure(figsize=(10,8))
df = data2[data2['Country']=='India']
sns.lineplot(x="Year", y="GDP per capita",data=df,label='India')
df = data2[data2['Country']=='United States']
sns.lineplot(x="Year", y="GDP per capita",data=df,label='US')
df = data2[data2['Country']=='Finland']
sns.lineplot(x="Year", y="GDP per capita",data=df,label='Finland')
df = data2[data2['Country']=='United Kingdom']
sns.lineplot(x="Year", y="GDP per capita",data=df,label="UK")
df = data2[data2['Country']=='Canada']
sns.lineplot(x="Year", y="GDP per capita",data=df,label='Canada')
plt.title("GDP per capita 2015-2019:")


# In[ ]:




