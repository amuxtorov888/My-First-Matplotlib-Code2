import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])
y1 = np.array([55, 60 ,65 ,62 ,68 ,70 ,75,78 ,82  ,85 ,87])


x2 = np.array([0,1,2,2,3,4,5,6,7,8,9])
y2 = np.array([50,58,65,70,72,78,83,88,92,95,98])


plt.scatter(x1,y1, color='blue', marker='o', s=200, alpha=0.7, edgecolors='black', 
            label='Student A')
plt.plot(x1,y1, color='red', linewidth=2, linestyle='dashed', alpha=0.5)

plt.scatter(x2,y2, color='green', marker='*', s=200, alpha=0.7, edgecolors='black', 
            label='Student B')
plt.plot(x2,y2, color='orange', linewidth=2, linestyle='dotted', alpha=0.5)

plt.title("Test Scores", fontsize=14, family='Arial', fontweight='bold', color='#2dbefc')
plt.xlabel("Hours Studied", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.ylabel("Test Scores", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.grid(axis='y', linewidth=2, color='lightgray', linestyle='dashdot', alpha=0.5)
plt.legend(loc='lower right', fontsize=10, frameon=True, facecolor='lightgray', edgecolor='black')
plt.show()