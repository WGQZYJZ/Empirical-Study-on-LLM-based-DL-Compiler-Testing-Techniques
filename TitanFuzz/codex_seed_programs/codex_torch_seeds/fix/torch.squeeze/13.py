'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input = torch.randn(1, 3, 1, 1)
print('Input data: \n', input)
output = torch.squeeze(input)
print('Output data: \n', output)