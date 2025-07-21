'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 5)
y = torch.arange(0, 5)
(x_mesh, y_mesh) = torch.meshgrid(x, y)
print(x_mesh)
print(y_mesh)