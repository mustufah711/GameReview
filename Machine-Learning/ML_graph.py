import matplotlib.pyplot as plt
import pandas as pd

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
