import numpy as np

## load npy data
arr = np.load('r_vs_t_surface.npy')

## write to csv where each point has x y and z
with open('r_vs_t_surface.csv', 'w') as f:
    f.write('x,y,z\n')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            f.write(f'{i},{j},{arr[i][j]}\n')

