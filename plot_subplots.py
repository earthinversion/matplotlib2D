import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# make fake data
x_orig = np.linspace(0, 4, 50) # points between 0 and 4

y_orig = np.exp(-x_orig) + 0.01*np.random.normal(size=len(x_orig)) # data is theory plus noise
y_orig2 = np.exp(-x_orig) + 0.05*np.random.normal(size=len(x_orig))
y_orig3 = np.exp(-x_orig) + 0.1*np.random.normal(size=len(x_orig))


fig, (ax1, ax2, ax3) = plt.subplots(3,1,figsize=(10,6),sharex=True)
ax1.plot(x_orig, y_orig, 'b', label='less noise', lw=1) # points
ax1.legend()

ax2.plot(x_orig, y_orig2, 'g', label='more noise', lw=1) # points
ax2.legend()
ax2.set_ylabel("Ylabel")

ax3.plot(x_orig, y_orig3, 'r', label='most noise', lw=1) # points
ax3.legend()
ax3.set_xlabel('Xlabel')

plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('multiple_plots.png',dpi=300,bbox_inches='tight')
plt.close('all')