'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
x = torch.randn(3, 1)
print(x)
y = torch.atleast_2d(x)
print(y)