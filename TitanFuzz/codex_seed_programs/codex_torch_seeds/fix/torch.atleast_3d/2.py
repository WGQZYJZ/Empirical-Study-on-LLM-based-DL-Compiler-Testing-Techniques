'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
import torch
x = torch.randn(1, 2, 1)
print(x)
print(torch.atleast_3d(x))
print(torch.atleast_3d(x, x))