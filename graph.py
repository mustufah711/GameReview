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

#axs = result[['IGN_Score','Dest_Score']].plot(kind='bar', title='Game Score', figsize=(10,10), fontsize=12)

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

#Database connection info
hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

#Storing game average results
score1 = []
score2 = []
score3 = []
score4 = []
score5 = []
score6 = []
score7 = []

#Running for fighter game genre
def dbRun(conn):
    cur = conn.cursor()
    cur.execute("select round(AVG(i.Score),2) as ign, round(AVG(d.Score),2) as dest from Destructoid d, (select distinct name, genre,score from IGN)i where d.name = i.name and i.Genre like '%Fighting%'")
    
    for scores1, scores2 in cur.fetchall():
        score1.append(scores1)
        score2.append(scores2)

#Running for RPG game genre
def dbRun2(conn):
    cur = conn.cursor()
    cur.execute("select round(AVG(i.Score),2) as ign, round(AVG(d.Score),2) as dest from Destructoid d, (select distinct name, genre,score from IGN)i where d.name = i.name and i.Genre like '%RPG%'")
    
    for scores1, scores2 in cur.fetchall():
        score3.append(scores1)
        score4.append(scores2)

def dbRun3(conn):
    cur = conn.cursor()
    cur.execute("select round(AVG(i.Score),2) as ign, AVG(d.Score) as dest, AVG(p.score) as poly from Destructoid d, Polygon p, (select distinct name, genre,score from IGN)i where d.name = i.name and p.name = i.name and i.Genre like '%Adventure%'")
    
    for scores1, scores2, scores3 in cur.fetchall():
        score5.append(scores1)
        score6.append(scores2)
        score7.append(scores3)

#Connect to mysql database
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn)
dbRun2(myConn)
dbRun3(myConn)
print(score3)

#Dictionary of result average scores for each genre
my_data = {'Figher':{'IGN':score1[0], 'Dest':score2[0]},
           'RPG':{'IGN':score3[0], 'Dest':score4[0]},
           'Adventure':{'IGN':score5[0], 'Dest':score6[0], 'Poly':score7[0]}}
#Conver to dataframe
df = pd.DataFrame(my_data)
#Graphing dataframe using Bar graph
axs = df.T.plot(kind='bar', figsize=(10,10), fontsize=12)
axs.set_xlabel("Genre Type", fontsize=12)
axs.set_ylabel("Average Score", fontsize=12)
plt.title('Genre Averages', fontsize=16)
plt.show()

myConn.close()