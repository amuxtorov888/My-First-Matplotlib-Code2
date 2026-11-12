import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2023,2024,2025,2026])
y1 = np.array([10, 20, 30, 40])

categories = np.array(['Grains','Fruits','Vegetables','Protein','Dairy','Sweets'])
values = np.array([4,3,2,5,1,3]) 

categories2 = ['Freshmen','Sophomore','Junior','Senior']
values2 = np.array([300,250,275,225])
colors2 = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

scores = np.random.normal(loc =80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x1, y1, marker='.', markersize=30, markerfacecolor='cyan', linestyle='dotted', linewidth=5, color='red')
axes[0, 0].set_title('Top Left')

axes[0, 1].bar(categories, values, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
axes[0, 1].set_title('Top Right')
axes[0, 1].set_xlabel('Food Categories', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
axes[0, 1].set_ylabel('Quantity', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')  

axes[1, 0].pie(values2, labels=categories2, autopct='%1.1f%%', colors=colors2, explode=[0.1, 0, 0, 0], shadow=True, startangle=90)
axes[1, 0].set_title('Bottom Left')


axes[1, 1].hist(scores, bins=10, color='blue', edgecolor='black', alpha=0.7)

axes[1, 1].set_title("Test Scores", fontsize=14, family='Arial', fontweight='bold', color='#2dbefc')
axes[1, 1].set_xlabel("Scores", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
axes[1, 1].set_ylabel("# of Students", fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')


plt.show() 