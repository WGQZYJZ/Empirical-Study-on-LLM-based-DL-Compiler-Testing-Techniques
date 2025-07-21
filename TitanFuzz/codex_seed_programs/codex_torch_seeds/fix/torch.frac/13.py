'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input data: \n', input)
output = torch.frac(input)
print('Output data: \n', output)