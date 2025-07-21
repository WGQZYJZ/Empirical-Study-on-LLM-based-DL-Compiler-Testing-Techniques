'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asinh\ntorch.asinh(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input: ', x)
print('Output: ', torch.asinh(x))