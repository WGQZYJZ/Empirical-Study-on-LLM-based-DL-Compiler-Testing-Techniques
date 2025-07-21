'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print(('-' * 20))
print('Task 2: Generate input data')
print(('-' * 20))
input = torch.randn(2, 3)
print('input = torch.randn(2, 3)')
print('input:')
print(input)
print('Task 3: Call the API torch.max')
print(('-' * 20))
print('torch.max(input, dim, keepdim=False, *, out=None)')
dim = 1
print('dim = 1')
print('torch.max(input, dim)')
print('torch.max(input, dim):')
print(torch.max(input, dim))
dim = 0
print('dim = 0')
print('torch.max(input, dim)')
print('torch.max(input, dim):')
print(torch.max(input, dim))
keepdim = True
print('keepdim = True')