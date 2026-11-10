import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['Grains','Fruits','Vegetables','Protein','Dairy','Sweets'])
values = np.array([4,3,2,5,1,3])  

plt.bar(categories, values, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])

plt.title('Daily Consumption', fontsize=16,family='Arial', fontweight='bold', color='blue')
plt.xlabel('Food Categories', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.ylabel('Quantity', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')

plt.show()