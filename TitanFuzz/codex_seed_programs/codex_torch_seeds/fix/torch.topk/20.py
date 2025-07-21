'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
a = torch.randn(5, 3)
print(a)
(values, indices) = torch.topk(a, 2)
print(values)
print(indices)
(values, indices) = torch.topk(a, 2, dim=1)
print(values)
print(indices)