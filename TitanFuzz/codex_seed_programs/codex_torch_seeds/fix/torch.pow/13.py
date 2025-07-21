'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('Input data: ', x)
y = torch.pow(x, 2)
print('Output data: ', y)
y = torch.pow(x, 2, out=x)
print('Output data: ', y)
print('Input data: ', x)
y = torch.pow(x, 3)
print('Output data: ', y)
y = torch.pow(x, 3, out=x)
print('Output data: ', y)
print('Input data: ', x)