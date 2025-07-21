'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
print('Input data: ', input)
output = torch.log10(input)
print('Output data: ', output)