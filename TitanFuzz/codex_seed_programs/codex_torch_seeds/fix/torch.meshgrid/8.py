'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 3)
y = torch.arange(0, 3)
(grid_x, grid_y) = torch.meshgrid(x, y)
print('x: ', x)
print('y: ', y)
print('grid_x: ', grid_x)
print('grid_y: ', grid_y)
print('grid_x.shape: ', grid_x.shape)
print('grid_y.shape: ', grid_y.shape)