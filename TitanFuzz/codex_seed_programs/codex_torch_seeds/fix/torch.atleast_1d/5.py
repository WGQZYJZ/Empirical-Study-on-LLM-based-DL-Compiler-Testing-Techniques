'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.randn(2, 1)
print(y)
z = torch.randn(1)
print(z)
print(torch.atleast_1d(x, y, z))