'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
input = torch.tensor([[True, False], [False, True]])
output = torch.logical_not(input)
print('Input:', input)
print('Output:', output)