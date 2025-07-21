'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 2)
print('input: ', input)
output = torch.min(input, dim=1)
print('output: ', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 2)
print('input: ', input)
output = torch.min(input, dim=1, keepdim=True)
print('output: ', output)