'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
input = torch.randn(4, 4)
print('Input data:\n', input)
output = torch.ravel(input)
print('Output data:\n', output)