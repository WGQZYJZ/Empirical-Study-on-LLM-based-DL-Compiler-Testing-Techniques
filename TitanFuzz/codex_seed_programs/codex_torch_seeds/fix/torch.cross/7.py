'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cross\ntorch.cross(input, other, dim=None, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 3)
other = torch.randn(4, 3)
print('Input: ', input)
print('Other: ', other)
print('Task 3: Call the API torch.cross')
output = torch.cross(input, other, dim=1)
print('Output: ', output)