#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:02:59 2017

download and save stock index data
"""

import datetime

## Add yahoo-finance fix
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override() ## Here is the fix



def save_data (pd_data, file_name):
    
    # Save Data by Converting Data to  CSV files
    pd_data.to_csv(file_name)





if __name__ == '__main__':
    
    # Create a lagged series of the S&P500 US stock market index
    start_date = datetime.datetime(1983,1,1)

    end_date  = datetime.datetime(2017,7,12)

    symbol_name = "^GSPC"   # S&P 500 US Stock index
    
    dir_name = '.'
    file_name = dir_name + "/" + symbol_name.lower().strip('^') + "_" + "ohlc_" + start_date.strftime('%Y-%m-%d') + "_to_" + end_date.strftime("%Y-%m-%d") + ".csv" 
    data = pdr.get_data_yahoo(symbol_name, start_date, end_date)
    
    save_data(data,file_name)
    
