'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
data = torch.randn(2, 1, 3)
print(data)
print(data.shape)
data = torch.randn(2, 1)
print(data)
print(data.shape)
data = torch.atleast_3d(data)
print(data)
print(data.shape)