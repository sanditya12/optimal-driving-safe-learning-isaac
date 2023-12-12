import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
from racing_data.left_boundary_points import left_boundary_points
from racing_data.right_boundary_points import right_boundary_points
from plotdata import trajectory_training_filter_911, trajectory_training_conventional
left_points_2d = [sublist[:2] for sublist in left_boundary_points]
right_points_2d = [sublist[:2] for sublist in right_boundary_points]

plt.axis([-3,3,-3,3])

x_l = [point[0] for point in left_points_2d]
y_l = [point[1] for point in left_points_2d]
 
x_r = [point[0] for point in right_points_2d]
y_r = [point[1] for point in right_points_2d]


for trajectory in trajectory_training_filter_911:
    x = [point[0] for point in trajectory]
    y = [point[1] for point in trajectory] 
    plt.plot(x,y, color = (0,0,1, 0.06))
 
# for trajectory in trajectory_training_conventional:
#     x = [point[0] for point in trajectory]
#     y = [point[1] for point in trajectory] 
#     plt.plot(x,y, color = (1,0,0, 0.06))


# Plot the line segments
plt.plot(x_l, y_l, color = '#808080')
plt.plot(x_r, y_r, color = '#808080')

# Add labels and show the plot
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajectories of Agent during Training with Safety Filter (100000 Timesteps)")
# plt.grid(True)
plt.show()