# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:29:46 2018

@author: Mustufa
"""
#https://stackoverflow.com/questions/29498652/plot-bar-graph-from-pandas-dataframe

"""
Graph idea: Get each site, get average for each genre and then graph it using bar
graph to compare the average scores between each site and see which site prefers a 
certain genre over another"
"""

"""
my_data = {1965:{'a':52, 'b':54, 'c':67, 'd':45}, 
      1966:{'a':34, 'b':34, 'c':35, 'd':76}, 
      1967:{'a':56, 'b':56, 'c':54, 'd':34}}  
A way to plot IGN, Gamespot, Destructoid, Polygon
"""

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
"""
hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

name = []
score = []
platform = []

def dbRun(conn):
    cur = conn.cursor()
    cur.execute("SELECT Name, Score, Platforms FROM Polygon WHERE Score >6 AND Platforms LIKE '%PS4%'")
    
    for names, scores, platforms in cur.fetchall():
        name.append(names)
        score.append(scores)
        platform.append(platforms)

myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn)
result = pd.DataFrame({'Name':name,
                       'Score': score,
                       'Platform':platform})

axs = result[['Name','Score']].plot(kind='line', title='Game Score', figsize=(10,10), fontsize=12)
axs.set_xlabel("Name", fontsize=12)
axs.set_ylabel("Score", fontsize=12)
plt.show()

myConn.close()
"""

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

name = []
score1 = []
score2 = []
platform = []

def dbRun(conn):
    cur = conn.cursor()
    cur.execute("select distinct i.Name, i.Score, d.Score from Destructoid d, IGN i where d.name = i.name and i.Genre = 'Shooter'")
    
    for names, scores1, scores2 in cur.fetchall():
        name.append(names)
        score1.append(scores1)
        score2.append(scores2)

myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn)
result = pd.DataFrame({'IGN_Score': score1,
                       'Dest_Score': score2})

axs = result[['IGN_Score','Dest_Score']].plot(kind='line', title='Game Score', figsize=(10,10), fontsize=12)
axs.set_xlabel("Shooter Games", fontsize=12)
axs.set_ylabel("Score", fontsize=12)
plt.show()

myConn.close()