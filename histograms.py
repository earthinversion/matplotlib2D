import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

means = 20, 50
stdevs = 4, 2
dist = pd.DataFrame(np.random.normal(loc=means, scale=stdevs, size=(1000, 2)),columns=['a', 'b'])

opacity = 0.5
bin_width = 0.8

fig, ax = plt.subplots()
# n, bins, patches = ax.hist(x=dist['a'], bins='auto', color='#0504aa',alpha=opacity, rwidth=bin_width)

dist.plot.kde(ax=ax, legend=False, title='My histogram', color=['r','b'])
dist.plot.hist(density=True,bins=22, alpha=opacity, ax=ax, backend='matplotlib', grid=True, color=['r','b'])
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.savefig('histograms.png',dpi=300,bbox_inches='tight')
plt.close('all')