'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
input = torch.randn(4)
print('Input data: ', input)
output = torch.asin(input)
print('Output data: ', output)