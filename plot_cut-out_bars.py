import matplotlib
import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'serif', 'weight': 'normal', 'size': 25}
matplotlib.rc('font', **font)

labels = ['0.', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
x = np.arange(len(labels))

graph = "BEER"

# 30 points between [0, 0.2) originally made using np.random.rand(30)*.2
# MAE
pts1 = np.array([3.8983,0.4688,0.4561,0.4422,0.4379,0.4355,0.4338,0.4337,0.4328,0.4291,0.429])
# RMSE
pts2 = np.array([3.9533,0.6375,0.6026,0.5883,0.5797,0.5817,0.5756,0.5761,0.5749,0.5737,0.5702])

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
f.set_figheight(8)
f.set_figwidth(10)
width = 0.2  # the width of the bars

# plot the same data on both axes
ax.bar(x-2*width, pts1, width, label='MAE', align='edge', alpha=.99)
ax.bar(x-width, pts2, width, label='RMSE', hatch="\\", align='edge', alpha=.99)

ax2.bar(x-2*width, pts1, width, label='MAE', align='edge', alpha=.99)
ax2.bar(x-width, pts2, width, label='RMSE', hatch="\\", align='edge', alpha=.99)

# zoom-in / limit the view to different portions of the data
ax.set_ylim(3.7, 4.0)  # outliers only
ax2.set_ylim(0.4, 0.7)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

#ax.tick_params(labelsize=20)
#ax2.tick_params(labelsize=20)

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

ax2.set_xlabel(r'$\lambda$', fontsize=25)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, fontsize=25)

ax.legend(loc=0, handletextpad=0.1, labelspacing=.1)
ax.set_title('Results for {} dataset'.format(graph), fontsize=35)
f.text(0.001, 0.5, 'error', va='center', rotation='vertical', fontsize=25)
f.tight_layout()
plt.xlim(0-2.5*width, len(x)-width)
plt.show()
outputfilename = 'Results_for_{}_dataset'.format(graph) + '_bar.jpg'
plt.savefig(outputfilename)