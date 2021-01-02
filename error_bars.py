import numpy as np
import matplotlib.pyplot as plt

# make fake data
x_orig = np.linspace(0, 4, 20) # points between 0 and 4
noise = 0.025*np.random.normal(size=len(x_orig)) # random numbers
y_orig = np.exp(-x_orig) + noise # data is theory plus noise


# including the error bar at each point
x_err = x_orig*0.1
y_err = y_orig*0.1

# add to plot the data as (x,y) with error bars
plt.errorbar(x_orig, y_orig, yerr = y_err, xerr = x_err, lw=1, 
             ecolor='g', fmt='o-', capthick=2, label='data')

# # let's also compare with the theoretical curve...
# xx = np.linspace(0, 1, 50)
# yy = np.exp(-3.*xx/2)
# # ...and add that to the plot as well
# plt.plot(xx, yy, lw=3, color='magenta', label='theory')

# it's nice if other people know what you did
plt.title('Experiment Results')
plt.ylabel('ylabel')
plt.xlabel('xlabel')
plt.legend()
plt.grid()

plt.savefig('error_bars.png',dpi=300,bbox_inches='tight')
plt.close('all')
