# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:41:35 2022

@author: thinkcentre1
"""
from forex_python.converter import CurrencyRates
import datetime

def get_data(conv_date):
    c = CurrencyRates()
    data = c.get_rate('USD', 'INR', conv_date)
    return data

a = get_data(datetime.datetime(2014, 5, 23, 18, 36, 28, 151012))
b = get_data(datetime.datetime(2014, 6, 23, 18, 36, 28, 151012))
c = get_data(datetime.datetime(2014, 7, 23, 18, 36, 28, 151012))
d = get_data(datetime.datetime(2014, 8, 23, 18, 36, 28, 151012))