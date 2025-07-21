'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input: ', input)
dim = 0
output = torch.amin(input, dim)
print('Output: ', output)
dim = 1
output = torch.amin(input, dim)
print('Output: ', output)