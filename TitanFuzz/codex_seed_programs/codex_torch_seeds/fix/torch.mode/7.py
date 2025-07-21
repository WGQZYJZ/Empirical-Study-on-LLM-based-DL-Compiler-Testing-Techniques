'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(1, 3)
print(input)
(value, indices) = torch.mode(input, dim=1)
print(value)
print(indices)