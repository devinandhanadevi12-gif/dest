import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([10,20,30,200])
ypoints = np.array([40,60,10,200])
plt.plot(xpoints,ypoints,marker='o')
plt.xlabel("X axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")
plt.grid()
plt.show()