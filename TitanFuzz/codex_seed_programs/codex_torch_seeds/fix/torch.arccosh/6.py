'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input = torch.rand(1, 3)
print('Input: ', input)
output = torch.arccosh(input)
print('Output: ', output)