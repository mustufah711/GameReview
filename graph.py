# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:29:46 2018

@author: Mustufa
"""

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

name = []
score = []
platform = []

def dbRun(conn):
    cur = conn.cursor()
    cur.execute("SELECT Name, Score, Platforms FROM Polylgon WHERE Score >5 AND Platforms LIKE '%PS4%' ORDER BY Score DESC ")
    
    for names, scores, platforms in cur.fetchall():
        name.append(names)
        score.append(scores)
        platform.append(platforms)

myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn)
result = pd.DataFrame({'Name': name,
                       'Score': score,
                       'Platform': platform})
print(result.head(2))

axs = result[['Name', 'Score']].plot(kind='line', title='Game Score', figsize=(15,10), fontsize=12)
axs.set_xlabel("Name", fontsize=12)
axs.set_ylabel("Score", fontsize=12)
plt.show()
myConn.close()