'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
x = torch.rand(4, 4)
print('Input: ', x)
y = torch.arccosh(x)
print('Output: ', y)