'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print(('-' * 10))
print('Task 2: Generate input data')
print(('-' * 10))
input = torch.randn(3, 3)
print('input: ')
print(input)
print('Task 3: Call the API torch.std')
print(('-' * 10))
std = torch.std(input, dim=1)
print('std: ')
print(std)
std = torch.std(input, dim=1, unbiased=False)
print('std: ')
print(std)