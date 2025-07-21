'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.randn(2, 3, 4)
y = torch.randn(2, 3, 4)
z = torch.randn(2, 3, 4)
print(torch.atleast_3d(x))
print(torch.atleast_3d(x, y))
print(torch.atleast_3d(x, y, z))