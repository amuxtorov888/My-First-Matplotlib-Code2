import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')

type_counts = data['Type1'].value_counts(ascending=True)
plt.barh(type_counts.index, type_counts.values, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])

plt.title("# Of Pokemon by Primary Type", fontsize=16,family='Arial', fontweight='bold', color='#2dbefc')
plt.xlabel('Number of Pokemon', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.ylabel('Types', fontsize=12, family='Arial', fontweight='bold', color='#2dbefc')
plt.tight_layout()

plt.show()