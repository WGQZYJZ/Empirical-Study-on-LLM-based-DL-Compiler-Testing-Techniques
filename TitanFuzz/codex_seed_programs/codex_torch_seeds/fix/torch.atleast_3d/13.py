'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.randn(2, 3)
print(x)
print(y)
print(z)
print(torch.atleast_3d(x, y, z))