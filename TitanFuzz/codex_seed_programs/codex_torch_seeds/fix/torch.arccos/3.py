'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
output = torch.arccos(input)
print('Output data: ', output)