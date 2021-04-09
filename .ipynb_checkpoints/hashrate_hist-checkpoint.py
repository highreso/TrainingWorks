#%matplotlib notebook
import matplotlib.pyplot as plt

n, bins, patches = plt.hist([298.8, 349.6, 338.5, 307.0, 355.5, 315.2, 363.3, 255.6, 342.5, 303.3, 285.6, 405.5, 395.2, 364.4, 306.6, 367.4, 314.4, 366.6, 350.7, 348.5, 358.5, 285.9, 332.6, 280.3, 294.4, 311.8, 334.8, 304.7])
plt.xlabel("Hashrate")
plt.ylabel("Freq")
plt.title("Hashrate_Histogram")
plt.show()
