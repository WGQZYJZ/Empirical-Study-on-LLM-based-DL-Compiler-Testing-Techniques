'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.randn(3, 5)
print(x)
print(x.shape)
x = torch.atleast_3d(x)
print(x.shape)