'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.heaviside\ntorch.heaviside(input, values, *, out=None)\n'
import torch
input = torch.randn(10)
print('input: ', input)
values = torch.randn(10)
print('values: ', values)
out = torch.heaviside(input, values)
print('out: ', out)