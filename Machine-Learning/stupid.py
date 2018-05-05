# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:23:27 2018

@author: HARSHA
"""

import mysql.connector
from sklearn import svm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = []
master_list = []

def dbRun(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    
    all_games = cur.fetchall()
    for i in all_games:
        game = []
        pubs = i[0].split(',')
        gens = i[1].split(',')
        devs = i[2].split(',')
        
        pub_sum = 0
        for item in pubs:
            pub_sum = (pub_sum + int(''.join([str(ord(a)) for a in item]))) / len(pubs)
        game.append(pub_sum)
        
        gen_sum = 0
        for k in gens:
            gen_sum = (gen_sum + int(''.join([str(ord(a)) for a in k]))) / len(gens)
        game.append(gen_sum)
        
        dev_sum = 0
        for j in devs:
            dev_sum = (dev_sum + int(''.join([str(ord(a)) for a in j]))) / len(devs)
        game.append(dev_sum)
        
        master_list.append(game)
        score.append(float(i[3]))
    cur.close()

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'
    
query1 = 'select publisher, genre, developer, score from Gamespot limit 200'
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn, query1)

clf = svm.SVC(gamma=0.019, C=50)
clf.fit(master_list[:-50], score[:-50])
print 'ML Prediction'
list1 = clf.predict(master_list[-50:])
list1 = list1.tolist()
print list1
print 'Expected Value'
expected = score[-50:]
print expected

count = 0
count2 = 0
for i in range(0, len(list1)):
    if(np.subtract(list1[i],expected[i]) == 0 or np.subtract(list1[i],expected[i]) == 1 or np.subtract(expected[i],list1[i]) == 1):
        count2 = count2+1
    if(np.subtract(list1[i],expected[i]) == 0):
        count = count+1
print 'ML Prediction Exact Match ', ((float(count)/len(list1)))
print 'ML Prediction Accuracy Close Match', ((float(count2)/len(list1)))