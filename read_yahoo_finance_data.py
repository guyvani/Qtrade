#!/usr/bin/python

from __future__  import print_function

import datetime

#USE GOOGLE FINANCE

##import pandas.io.data as wb
#import pandas_datareader.data as wb
#
#
##if __name__ == "__main__":
#spy = wb.DataReader(
#           "SPY", "google",
#            datetime.datetime(2007, 1, 1),
#            datetime.datetime(2016, 10,17)
#    )
#print(spy.tail())


## USE YAHOO FINANCE
'''
 To use yahoo you must first fix the issue with pandas_datareader
 by installing the following:

git clone https://github.com/ranaroussi/fix-yahoo-finance.git
cd fix-yahoo-finance/
python setup.py install

'''

#Now use it as follows:
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override() ## Here is the fix

symbol = "AMZN"
startDate = datetime.datetime(2007,1,1)
endDate = datetime.datetime(2017,7,12)

## download the DataFrame
pd_data = pdr.get_data_yahoo(symbol, start = startDate, end=endDate)

##print(pd_data.head())
#Download the Panel
data_panel = pdr.get_data_yahoo([symbol, "IWM"], start = startDate, end=endDate)

# Save Data by Converting Data to  CSV files
dirName = "./data_test"
fileName = dirName + "/" + symbol.lower() + "_" + "ohlc_" + startDate.strftime('%Y-%m-%d') + "_to_" + endDate.strftime("%Y-%m-%d") + ".csv"

pd_data.to_csv(fileName)


## Read Data as csv file
import pandas as pd
df = pd.read_csv(fileName, index_col='Date', parse_dates=True)
print(df.head())


