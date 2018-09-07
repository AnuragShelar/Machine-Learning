import pandas as pd
import quandl
quandl.ApiConfig.api_key ='nxAhf4MWnT7KnBxVy3YZ'

df=quandl.get('WIKI/GOOGL')

#keeping only those colomns which we need 
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]


df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/(df['Adj. Close'])*100.0

df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/(df['Adj. Open'])*100.0

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())