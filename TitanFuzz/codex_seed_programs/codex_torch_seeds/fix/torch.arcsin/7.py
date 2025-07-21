'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
a = torch.randn(4)
print('Input: ', a)
output = torch.arcsin(a)
print('Output: ', output)