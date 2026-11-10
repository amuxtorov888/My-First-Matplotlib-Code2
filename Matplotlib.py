import matplotlib.pyplot as plt
import numpy as np

categories = ['Freshmen','Sophomore','Junior','Senior']
values = np.array([300,250,275,225])
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.pie(values,labels = categories,
        autopct = '%1.1f%%',
        colors=colors,
        explode = [0.1,0,0,0],
        shadow = True,
        startangle = 90)

plt.title('Akmal College', fontsize=16,family='Arial', fontweight='bold', color='blue')

plt.show()