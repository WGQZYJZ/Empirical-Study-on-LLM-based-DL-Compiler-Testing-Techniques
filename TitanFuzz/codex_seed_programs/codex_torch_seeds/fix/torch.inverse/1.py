'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print('Input data: ', input)
output = torch.inverse(input)
print('Output data: ', output)