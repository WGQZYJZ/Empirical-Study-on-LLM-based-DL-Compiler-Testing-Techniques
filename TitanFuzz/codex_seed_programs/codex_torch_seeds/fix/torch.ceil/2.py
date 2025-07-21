'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: \n', input)
print('Output: \n', torch.ceil(input))