# The following only requires 
# the python extension and ipython installed
## use the following syntax
## #%% (Start cell) 
# <code to execute>
## #%% (Start next cell) (End previous cell)

#%%
import pandas as pd
import os
os.getcwd()

#%%
avocados = pd.read_csv("data/avocado.csv")
avocados.drop("X1",axis=1).head()

#%%
subset = avocados.query("region < 'B'")\
    .query("type=='conventional'")

subset['Date'] = pd.to_datetime(subset.Date)
subset = subset.sort_values("Date")
subset.head()

#%%
import plotly.express as px

px.line(subset,x="Date",y="AveragePrice")

## Odd plot maybe someone can improve it...

# %%
