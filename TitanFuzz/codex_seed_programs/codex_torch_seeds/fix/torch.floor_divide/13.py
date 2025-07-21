'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print('Input 1: ', x)
print('Input 2: ', y)
z = torch.floor_divide(x, y)
print('Result: ', z)