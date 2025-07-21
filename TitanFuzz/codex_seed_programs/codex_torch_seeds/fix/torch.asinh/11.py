'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asinh\ntorch.asinh(input, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print('Input: ', a)
b = torch.asinh(a)
print('Output: ', b)