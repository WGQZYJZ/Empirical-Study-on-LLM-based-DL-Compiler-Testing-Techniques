'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('input: ', input)
output = torch.pow(input, 2)
print('output: ', output)