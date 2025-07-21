'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
x = torch.randn(2, 3, 4)
print('Input data: ', x)
y = torch.flip(x, dims=[0])
print('Output data: ', y)
y = torch.flip(x, dims=[1])
print('Output data: ', y)
y = torch.flip(x, dims=[0, 1])
print('Output data: ', y)
y = torch.flip(x, dims=[0, 2])
print('Output data: ', y)