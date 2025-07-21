'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input: ', input)
dim = 0
print('Dim: ', dim)
print('Output: ', torch.amin(input, dim))
dim = 1
print('Dim: ', dim)
print('Output: ', torch.amin(input, dim))