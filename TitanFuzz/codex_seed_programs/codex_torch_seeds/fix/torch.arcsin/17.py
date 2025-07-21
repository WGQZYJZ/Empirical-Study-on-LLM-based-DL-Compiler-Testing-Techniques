'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
import torch
x = torch.randn(4)
print('Input data is: ', x)
y = torch.arcsin(x)
print('Output data is: ', y)