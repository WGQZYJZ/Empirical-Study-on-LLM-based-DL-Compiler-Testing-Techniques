'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
a = torch.rand(4, 4)
print(a)
mean = torch.mean(a, dim=1, keepdim=True)
print(mean)