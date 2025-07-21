'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
data = torch.rand(3, 4)
print('Input data: ', data)
print('Output data: ', torch.pow(data, 2))