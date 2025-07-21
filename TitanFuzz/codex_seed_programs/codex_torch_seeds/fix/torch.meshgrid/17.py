'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 3, 1)
y = torch.arange(0, 3, 1)
(grid_x, grid_y) = torch.meshgrid(x, y)
print('grid_x:', grid_x)
print('grid_y:', grid_y)