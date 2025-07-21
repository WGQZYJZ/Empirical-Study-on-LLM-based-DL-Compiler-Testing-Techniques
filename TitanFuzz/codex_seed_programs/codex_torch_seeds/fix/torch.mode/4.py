'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input data:\n', input)
(mode, indices) = torch.mode(input, dim=1)
print('Mode:\n', mode)
print('Indices:\n', indices)