import matplotlib.pyplot as plt
import numpy as np
import sys

# 30 points between [0, 0.2) originally made using np.random.rand(30)*.2

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)
fig.set_figheight(8)
fig.set_figwidth(10)
labels = ['0.', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
xlabels = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
x = np.arange(len(labels))
mae_values = np.array([4.1388, 0.781, 0.768, 0.762, 0.762, 0.761, 0.763, 0.764, 0.772, 0.775, 0.779])
rmse_values = np.array([4.2829, 0.977, 0.976, 0.975, 0.977, 0.977, 0.971, 0.971, 0.980, 0.968, 0.969])

ax_linemae = ax.plot(x, mae_values)
ax_linermse = ax.plot(x, rmse_values)

ax2_linemae = ax2.plot(x, mae_values)
ax2_linermse = ax2.plot(x, rmse_values)

# Zoom-in / limit the view to different portions of the data
ax.set_ylim(4.0, 4.3)   # Outliers
ax2.set_ylim(0.75, 1.0) # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.xaxis.tick_top()
ax.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_xlabel(r'$\lambda$')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax.legend(fontsize="x-small", loc=0, handletextpad=0.1, labelspacing=.1)

plt.show()
