'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.acosh(input)
print('Output: ', output)