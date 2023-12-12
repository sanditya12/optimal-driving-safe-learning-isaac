import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
from plotdata import interventions

episodes = [i for i in range(len(interventions))]


# Plot the line segments
plt.plot(episodes, interventions, color = '#808080')

# Add labels and show the plot
plt.xlabel("Episodes")
plt.ylabel("Interventions")
plt.title("Interventions Frequency per Episode in Learning with Safety Filter (100000 Timesteps)")
# plt.grid(True)
plt.show()