import numpy as np
import pandas as pd
from datetime import datetime
from pandas_datareader import DataReader

rand_array = np.random.rand(3, 3)
df = pd.DataFrame(data=rand_array, columns=['a', 'b', 'c'])
print(df)

# 取得する期間
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
print(end)

AAPL = DataReader('AAPL', 'yahoo', start, end)
# print(AAPL)

# AAPL.info()

# print(AAPL['Adj Close'].plot(legend=True, figsize=(10, 4)))