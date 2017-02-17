#!/usr/bin/env python
import pandas as pd
from pandas_datareader import data


df = pd.read_csv('SIX-CH0350494719CHF4.csv')
# print(df.head(50))

df.set_index('Date', inplace=True)

df.to_csv('newcsv.csv')
