'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.linspace(0, 1, steps=5)
y = torch.linspace(0, 1, steps=5)
print(x)
print(y)
(x_mesh, y_mesh) = torch.meshgrid(x, y)
print(x_mesh)
print(y_mesh)