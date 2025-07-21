'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
data = torch.randn(3, 4)
print(torch.reciprocal(data))
print(torch.reciprocal(data, out=data))
print(data)
'\nTask 4: Call the API torch.reciprocal_\ntorch.reciprocal_(input)\n'
data = torch.randn(3, 4)
print(torch.reciprocal_(data))
print(data)