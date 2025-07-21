'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
import torch
x = torch.randn(4)
print('x = ', x)
y = torch.log(x)
print('y = ', y)