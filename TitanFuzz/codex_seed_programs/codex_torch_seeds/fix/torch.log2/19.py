'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('Input data: ', x)
output = torch.log2(x)
print('Output data: ', output)