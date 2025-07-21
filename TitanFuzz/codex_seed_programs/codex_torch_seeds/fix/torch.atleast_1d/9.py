'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
x = torch.rand(2, 3)
print(x)
y = torch.atleast_1d(x)
print(y)
y = torch.atleast_1d(x, x)
print(y)