#!/usr/bin/env python
from pandas_datareader import data, wb
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = data.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
