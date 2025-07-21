'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
import torch
x = torch.rand(2, 3)
print(x)
out = torch.atleast_3d(x)
print(out)
out = torch.atleast_3d(x, x, x)
print(out)
out = torch.atleast_3d(x, x, x, x)
print(out)