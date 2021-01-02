import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# make fake data
x_orig = np.linspace(0, 4, 20) # points between 0 and 4
noise = 0.025*np.random.normal(size=len(x_orig)) # random numbers
y_orig = np.exp(-x_orig) + noise # data is theory plus noise

# create theoretical curve to compare with "data"
x_pred = np.linspace(min(x_orig),max(x_orig), 200) # use more values to get smooth curve
y_pred = np.exp(-x_pred)

# setup the plots: both points and smooth curve       
fig= plt.figure()                 
plt.plot(x_orig, y_orig, 'bo', label='data', lw=3) # points
plt.plot(x_pred, y_pred, color='green', label='pred', lw=3) # line
# plt.grid() #can use this if the style is not imported
plt.legend()
plt.xlabel('x')
plt.ylabel('Original vs Predicted')
plt.title("Results")
# plt.yscale('log') # make the y axis (ordinate) log; that is, log-linear

plt.savefig('simple_plot_non_log.png',dpi=300,bbox_inches='tight')
plt.close('all')


### Plot 2
fig= plt.figure()
# setup the plots: both points and smooth curve                        
plt.plot(x_orig, y_orig, 'bo', label='data', lw=3) # points
plt.plot(x_pred, y_pred, color='green', label='pred', lw=3) # line
# plt.grid() #can use this if the style is not imported
plt.legend()
plt.xlabel('x')
plt.ylabel('Original vs Predicted')
plt.title("Results")
plt.yscale('log') # make the y axis (ordinate) log; that is, log-linear

plt.savefig('simple_plot.png',dpi=300,bbox_inches='tight')
plt.close('all')