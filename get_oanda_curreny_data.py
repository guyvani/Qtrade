#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:24:41 2017

Download Currency Historical Data from Oanda

"""


from pandas_datareader.oanda import get_oanda_currency_historical_rates

start, end = "2015-01-01", "2017-07-11"

quote_currency = "USD"

base_currency = ["EUR", "GBP", "JPY"]

#rates as a Pandas DataFrame
df_rates = get_oanda_currency_historical_rates(

            start,
            end, 
            quote_currency = quote_currency,
            base_currency = base_currency

)

print(df_rates.head())
