import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc =80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10, color='blue', edgecolor='black', alpha=0.7)

plt.title("Test Scores", fontsize=14, family='Arial', fontweight='bold', color='#2dbefc')
plt.xlabel("Scores", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.ylabel("# of Students", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')

plt.show()