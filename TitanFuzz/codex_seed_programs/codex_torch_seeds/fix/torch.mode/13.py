'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: \n', input)
mode = torch.mode(input, dim=1)
print('Mode: \n', mode)