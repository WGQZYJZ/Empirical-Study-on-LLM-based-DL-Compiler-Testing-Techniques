'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 5)
print('Input: {}'.format(input))
print('Task 3: Call the API torch.std')
result = torch.std(input)
print('Result: {}'.format(result))