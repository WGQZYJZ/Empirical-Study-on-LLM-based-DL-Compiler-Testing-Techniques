'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
print('Task 1: import PyTorch')
print(torch.__version__)
print('Task 2: Generate input data')
input = torch.randn(3, 3)
print(input)
print('Task 3: Call the API torch.nonzero')
output = torch.nonzero(input)
print(output)