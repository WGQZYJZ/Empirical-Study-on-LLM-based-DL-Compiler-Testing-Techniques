'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(1, 3, 3)
print('input: ', input)
output = torch.median(input, dim=(- 1), keepdim=False)
print('output: ', output)