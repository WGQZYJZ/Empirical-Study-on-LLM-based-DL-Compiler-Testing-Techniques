'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_conj\ntorch.is_conj(input)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 4)
print('Task 3: Call the API torch.is_conj')
print(torch.is_conj(input))