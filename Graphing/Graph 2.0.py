# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 11:29:46 2018

@author: Mustufa
"""
#https://stackoverflow.com/questions/29498652/plot-bar-graph-from-pandas-dataframe

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

#Running for game genres
def dbRun(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    
    for scores1, scores2, scores3 in cur.fetchall():
        score1.append(scores1)
        score2.append(scores2)
        score3.append(scores3)
    cur.close()

#Connect to mysql database
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)

query1 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%Fighting%'"""
query2 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%RPG%'"""
query3 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%Adventure%'"""
query4 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%Action%'"""
query5 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%Platformer%'"""
query6 = """select round(AVG(i.Score),2) as ign, round(AVG(g.Score),2) as Gamespot, round(AVG(d.score),2) as Dest
        from Gamespot g, (select distinct name, genre,score from IGN)i, Destructoid d 
        where g.name = i.name and d.name = i.name and i.Genre like '%Sports%'"""        

dbRun(myConn,query1)
dbRun(myConn,query2)
dbRun(myConn,query3)
dbRun(myConn,query4)
dbRun(myConn,query5)
dbRun(myConn,query6)

#Dictionary of result average scores for each genre
my_data = {'Fighter':{'IGN':score1[0], 'Gamespot':score2[0], 'Dest':score3[0]},
           'RPG':{'IGN':score1[1], 'Gamespot':score2[1], 'Dest':score3[1]},
           'Adventure':{'IGN':score1[2], 'Gamespot':score2[2], 'Dest':score3[2]},
           'Action':{'IGN':score1[3], 'Gamespot':score2[3], 'Dest':score3[3]},
           'Platformer':{'IGN':score1[4], 'Gamespot':score2[4], 'Dest':score3[4]},
           'Sports':{'IGN':score1[5], 'Gamespot':score2[5], 'Dest':score3[5]}}
#Conver to dataframe
df = pd.DataFrame(my_data)
#Graphing dataframe using Bar graph
axs = df.T.plot(kind='bar', figsize=(12,12), fontsize=12)
axs.set_xlabel("Genre Type", fontsize=13)
axs.set_ylabel("Game Rating Averages", fontsize=13)
plt.title('Game Genre Averages', fontsize=16)
plt.show()

myConn.close()