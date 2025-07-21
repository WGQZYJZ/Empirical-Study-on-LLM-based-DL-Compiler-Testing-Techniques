'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(100, 5)
(mode, indices) = torch.mode(input, dim=(- 1), keepdim=False)
print('mode: ', mode)
print('indices: ', indices)