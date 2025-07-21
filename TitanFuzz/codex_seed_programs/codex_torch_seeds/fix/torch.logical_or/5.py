'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_or\ntorch.logical_or(input, other, *, out=None)\n'
import torch
import torch
input = torch.tensor([[True, False], [False, False]])
other = torch.tensor([[False, False], [True, False]])
output = torch.logical_or(input, other)
print('Input 1:', input)
print('Input 2:', other)
print('Output:', output)