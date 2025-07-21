'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
print('Task 3: Call the API torch.mm')
print('torch.mm(input, mat2, *, out=None)')
print(torch.mm(input, mat2))