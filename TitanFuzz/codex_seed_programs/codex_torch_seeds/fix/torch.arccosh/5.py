'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
import math
input = torch.randn(3, 3)
output = torch.arccosh(input)
print('Input: ', input)
print('Output: ', output)