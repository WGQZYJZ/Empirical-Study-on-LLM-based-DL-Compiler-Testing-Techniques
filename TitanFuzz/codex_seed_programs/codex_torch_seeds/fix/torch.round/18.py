'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 4, 4)
print('Input:', input)
print('Input type:', type(input))
output = torch.round(input)
print('Output:', output)
print('Output type:', type(output))