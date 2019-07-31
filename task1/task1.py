import numpy as np
x = np.loadtxt('data.txt')
print("%.2f" % np.percentile(x, 90))
print("%.2f" % np.percentile(x, 50))
print("%.2f" % max(x))
print("%.2f" % min(x))
print("%.2f" % np.mean(x))

