'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
y = torch.tensor([5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
(grid_x, grid_y) = torch.meshgrid(x, y)
print('grid_x = ', grid_x)
print('grid_y = ', grid_y)