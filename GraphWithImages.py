import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("YellowSpaceSubmarine.png")

fig, ax = plt.subplots()
ax.imshow(img, extent=(-5, 5, -5, 5), alpha=0.3)

x = np.linspace(-5,5,100)
ax.plot(x, np.sin(x))
ax.set_title("Graph with Image Background")

plt.show()