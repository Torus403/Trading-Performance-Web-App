import pandas as pd
from alpha_vantage import alphavantage
import time
import matplotlib.pyplot as plt

api_key = 'E5FQSTJUMCK5S4DO'
ts = TimeSeries(key=api_key, output_format='pandas')

data, meta_data = ts.get_intraday(symbol='TSLA', interval = '1min', outputsize = 'full')
print(data)

