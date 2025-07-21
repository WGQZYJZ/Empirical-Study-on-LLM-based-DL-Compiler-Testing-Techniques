'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input = torch.randn(3, 3)
print('Input data: ', input)
print('Task 3: Call the API torch.inverse')
out = torch.inverse(input)
print('Output data: ', out)