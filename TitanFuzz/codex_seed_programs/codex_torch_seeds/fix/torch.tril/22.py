'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 3)
print('input:')
print(input)
print('Task 3: Call the API torch.tril')
output = torch.tril(input)
print('output:')
print(output)