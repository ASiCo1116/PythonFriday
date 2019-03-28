import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np

plt.xkcd()
fig = plt.figure()
plt.xlim((0,2))
plt.ylim((0,2))
ax = fig.add_subplot(111)
ax.set_aspect('equal')
A = pat.Arc(xy = (1.75,1.25), width = 1, height = 1 , theta1 = 90 ,theta2 = 180, linewidth = 20
	, edgecolor = '#ffffff')
ax.add_patch(A)
plt.vlines(1.25, 0, 1.25, colors = "#ffffff", linewidth = 20)
plt.hlines(1.10, 0.85, 1.75, colors = "#ffffff", linewidth = 20)
ax.patch.set_facecolor('#0066cc')
plt.show()