import matplotlib.pyplot as plt
import numpy as np
'''
## Parameters
bar_width = 0.25
opacity=0.5

fig, ax = plt.subplots()

langs = ['Sub-1', 'Sub-2', 'Sub-3', 'Sub-4', 'Sub-5']
students = [23,17,35,29,12]
ax.bar(langs,students, color='orange', alpha=opacity)

plt.savefig('bar_plots.png',dpi=300,bbox_inches='tight')
plt.close('all')


## Plot 2
data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)

fig, ax = plt.subplots()
ax.bar(X, data[0], color = 'b', width = 0.22, label='A')
ax.bar(X + bar_width, data[1], color = 'g', width = 0.22, label='B')
ax.bar(X + 2*bar_width, data[2], color = 'r', width = 0.22, label='C')
plt.legend()
plt.xticks(X + bar_width,X)
plt.savefig('bar_plots2.png',dpi=300,bbox_inches='tight')
plt.close('all')
'''


opacity=0.5
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) # the x locations for the groups
bar_width = 0.25


fig, ax = plt.subplots()
ax.bar(ind, menMeans, bar_width, color='r', alpha=opacity)
ax.bar(ind, womenMeans, bar_width, bottom=menMeans, color='b', alpha=opacity)
ax.set_ylabel('Scores')
ax.set_title('Here goes the title')
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=['Men', 'Women'])
ax.grid(color='gray', alpha=opacity, linestyle='dashed')

## Text and arrow on a plot
plt.text(1.5, 65, 'My custom\n text here', size=8)
plt.arrow(1.5, 65, -1.5, -40, shape='full', lw=2)

plt.xticks(ind,('G1', 'G2', 'G3', 'G4', 'G5'))

plt.savefig('stacked_bar.png',dpi=300,bbox_inches='tight')
plt.close('all')