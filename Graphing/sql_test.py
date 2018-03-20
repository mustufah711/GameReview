# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:15:10 2018

@author: Mustufa
"""

#https://www.a2hosting.com/kb/developer-corner/mysql/connecting-to-mysql-using-python

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

hostname = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com'
username = 'student'
password = 'cs336student'
database = 'BarBeerDrinker'

barTable = []
beerTable = []
price = []

def db(conn):
    cur = conn.cursor()
    cur.execute("Select distinct s.beer, a.name, s.price From bars a, sells s Where a.name = s.bar AND s.price < 5 ")
    
    for beers, bars, prices in cur.fetchall():
        beerTable.append(beers)
        barTable.append(bars)
        price.append(float(prices))
        
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
db(myConn)
result = pd.DataFrame({'Beer': beerTable,
                       'Bar': barTable,
                       'Price': price})

plt.plot(result)
myConn.close()
    