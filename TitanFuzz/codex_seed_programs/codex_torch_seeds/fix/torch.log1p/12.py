'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
x = torch.randn(5, 3)
print('Input data:')
print(x)
y = torch.log1p(x)
print('Output data:')
print(y)