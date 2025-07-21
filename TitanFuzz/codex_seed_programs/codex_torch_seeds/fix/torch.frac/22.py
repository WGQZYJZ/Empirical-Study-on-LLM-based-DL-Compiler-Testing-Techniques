'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input data: ', input)
output = torch.frac(input)
print('Output data: ', output)