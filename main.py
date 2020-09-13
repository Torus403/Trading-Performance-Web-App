import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'E5FQSTJUMCK5S4DO'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol = 'GSK', interval = '1min', outputsize = 'compact')
print(data)