#criar cenario
import numpy as np
import random
from matplotlib import pyplot as plt
space_x = 100
space_y = 100
quant_blocks = 15
space_grid = []
id = 0
block_off_id = np.random.randint((space_x * space_y),size=(quant_blocks));
for x in range(space_x):
    for y in range(space_y):
        id = id+1
        space_grid.append(
            {
                'id': id,
                'x' : x,
                'y' : y,
                'block': 1 if (True==id in block_off_id) else 0
            }
        )
        id = id + 1
#plot cenarios
plt.xlim(0,space_x)
plt.ylim(0,space_y)
# plt.grid()
ploty=[]
plotx=[]
for boff in block_off_id:
    plotx.append(
        space_grid[boff]['x']
    )
    ploty.append(
        space_grid[boff]['y']
    )

#PLOTS======================================>

fig = plt.figure()
ax = plt.axes(projection="3d")

num_bars = 15
x_pos = plotx
y_pos = ploty
z_pos = [0] * num_bars


#PLOT predios==============================>
x_size = np.ones(num_bars)*10
y_size = np.ones(num_bars)*10
z_size = random.sample(range(10,30), num_bars)
ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='aqua')

#PLOT UAVs=================================>
z_points = [10, 15]
x_points = [55, 80]
y_points = [35, 70]
ax.scatter(x_points, y_points, z_points, c='r', marker='*');
plt.show()

