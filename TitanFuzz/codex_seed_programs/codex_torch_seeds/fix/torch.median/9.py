'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
output = torch.median(input)
print('Output data: ', output)