'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input = torch.randn(5, 3)
print(input)
cummin = torch.cummin(input, dim=1)
print(cummin)