import matplotlib.pyplot as plt
import csv
import pandas as pd

x = []
y = []
z = []

with open('10000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[1]))
        y.append((row[2]))
        z.append((row[0]))

x = x[1:]
y = y[1:]
z = z[1:]

for i in range(0,1000):
    x[i]=int(x[i])
    y[i]=int(y[i])
    z[i]=int(z[i])

master_list = []
master_list = [41.8, 83.2, 12.68, 21.63, 42.2, 84.8]
#master_list.append(z)

#data = {'Actual':{master_list[0]},
       #'Iteration':{master_list[2]}}
my_data = {'Pub/Genre':{'Exact Match':master_list[0], 'Relative Match':master_list[1]},
           'Pub/Gen/Dev':{'Exact Match':master_list[4], 'Relative Match':master_list[5]},
           'Failed':{'Exact Match':master_list[2], 'Relative Match':master_list[3]}}
df = pd.DataFrame(my_data)
#Graphing dataframe using Bar graph
axs = df.T.plot(kind='bar', figsize=(8,8), fontsize=12)
axs.set_xlabel("Testing Results", fontsize=13)
axs.set_ylabel("Predictive Algorithm Scores", fontsize=13)
plt.title('Supervised Learning Experiment', fontsize=16)
plt.show()
