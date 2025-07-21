'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(5)
print('Input data: ', input)
output = torch.remainder(input, 2)
print('Output data: ', output)