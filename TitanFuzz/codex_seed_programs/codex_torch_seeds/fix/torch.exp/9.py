'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('Input data: ', x)
output = torch.exp(x)
print('Output data: ', output)