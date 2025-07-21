'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
inp = torch.randn(3, 3)
print('Input: \n', inp)
print('Diagonal: \n', torch.diagonal(inp))