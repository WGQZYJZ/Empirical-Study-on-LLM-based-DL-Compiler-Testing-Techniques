'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('Task 2: Generate input data')
input = torch.rand(2, 2)
print('Input data: {}'.format(input))
print('Task 3: Call the API torch.median')
print('torch.median(input, dim=-1, keepdim=False, *, out=None)')
print('Median of input data: {}'.format(torch.median(input)))