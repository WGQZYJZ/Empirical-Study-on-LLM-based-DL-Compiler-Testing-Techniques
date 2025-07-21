'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.cosh(input)
print('Output: ', output)
print('Output shape: ', output.shape)