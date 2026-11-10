import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,15,20])
y2 = np.array([10,20,25,15])
y3 = np.array([5,10,15,20])

line_style =dict(marker='.', markersize=30, markerfacecolor='blue', 
         linestyle='dashed', linewidth=5)

plt.plot(x, y1, marker='.', markersize=30, markerfacecolor='cyan', linestyle='dotted', linewidth=5, color='red')
plt.plot(x, y2,color = '#1cfc45',**line_style)
plt.plot(x, y3, color = '#1cfc45',**line_style)

plt.show()   