'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.linspace(0, 1, steps=5)
y = torch.linspace(0, 1, steps=7)
(grid_x, grid_y) = torch.meshgrid(x, y)
print(grid_x)
print(grid_y)