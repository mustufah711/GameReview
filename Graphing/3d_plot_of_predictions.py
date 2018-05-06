from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pandas as pd


db = pd.read_csv('devs_pubs_10k.csv')
fig = plt.figure(figsize=(20,10))
ax = plt.axes(projection='3d')

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8]

ax.set_xlabel('Index')
ax.set_ylabel('Expected')
ax.set_zlabel('Prediction')
ax.scatter3D(db.index, db.Expected, db.Prediction)
