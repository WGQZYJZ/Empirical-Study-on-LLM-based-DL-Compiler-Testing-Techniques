'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erf\ntorch.erf(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input data: ', x)
y = torch.erf(x)
print('Output data: ', y)