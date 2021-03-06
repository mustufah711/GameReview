
import mysql.connector
from sklearn import svm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = []
master_list = []

def dbRun(conn, query):
    j = 0
    cur = conn.cursor()
    cur.execute(query)
    
    all_games = cur.fetchall()
    for i in all_games:
        game = []
        pubs = i[0].split(',')
        gens = i[1].split(',')
    
        sum1 = 0
        count = 0
        for item in pubs:
            cur2 = conn.cursor()
            query2 = 'select avg(score) from Gamespot where publisher like '+'"%'+item +'%"'
            cur2.execute(query2)
            for f in cur2.fetchall():
                f = str(f)
                f = f[1:-2]
                if f=='None':
                    f = 0
                    sum1 = sum1+f
                else:
                    f = float(f)
                    sum1 = sum1+f
                    count = count+1
        if(count==0):
            sum1 = sum1/len(pubs)
        else:
            sum1 = sum1/count
        game.append(long(sum1))
        
        sum2 = 0
        count1 = 0
        for items in gens:
            cur1 = conn.cursor()
            query1 = 'select avg(score) from Gamespot where genre like '+'"%'+items +'%"'
            cur1.execute(query1)
            for z in cur1.fetchall():
                z = str(z)
                z = z[1:-2]
                if z=='None':
                    s = 0
                    sum2 = sum2+s
                else:
                    s = float(z)
                    sum2 = sum2+s
                    count1 = count1+1
        if(count1==0):
            sum2 = sum2/len(gens)
        else:
            sum2 = sum2/count1
        game.append(long(sum2))
        
        j=j+1
        if j%100==0:
            print 'iteration at ', j
        a = long(i[3])
        game.append(a)
        master_list.append(game)
        score.append(int(i[2]))
    cur.close()
    cur1.close()
    cur2.close()

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'
    
query1 = 'select publisher, genre, score, userscore from Gamespot limit 5000'
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
dbRun(myConn, query1)

#Machine Learning Section
clf = svm.SVC(gamma=0.019, C=50)
clf.fit(master_list[:-1000], score[:-1000])
print 'ML Prediction'
list1 = clf.predict(master_list[-1000:])
list1 = list1.tolist()
print list1
print 'Expected Value'
expected = score[-1000:]
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
