'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagflat\ntorch.diagflat(input, offset=0)\n'
import torch
input = torch.rand(3, 3)
print('Input data: ', input)
output = torch.diagflat(input)
print('Output data: ', output)