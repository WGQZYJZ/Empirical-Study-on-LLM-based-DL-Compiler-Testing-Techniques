'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
input = torch.randn(10)
print('The input data is: ', input)
output = torch.expm1(input)
print('The output data is: ', output)