'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.rand(3, 3)
print('Input: \n', input)
print('\n')
dim = 0
print('Output: \n', torch.cumprod(input, dim))