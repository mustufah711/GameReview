from sklearn import datasets
from sklearn import svm
import pickle
import mysql.connector
"""
iris = datasets.load_iris()
digits = datasets.load_digits()

print digits.target
print digits.images[0]

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1]) 
print clf.predict(digits.data[-1:])

X,y = iris.data, iris.target
print clf.fit(X,y)

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print clf2.predict(X[0:1])
"""

str1 = 'mustufa'
print(int(''.join([str(ord(a)) for a in str1])))

total_val = []
i = 0

def dbRun(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    
    for publishers in cur.fetchall():
        publisher.append(publishers)
        item = ''
        for item in publisher:
            
    cur.close()

hostname = 'game-reviews.cix4c2nzx8tc.us-east-2.rds.amazonaws.com'
username = 'gamers'
password = 'mostharsh'
database = 'GameReviews'

query1 = 'select publisher from Gamespot'
myConn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)

dbRun(myConn, query1)