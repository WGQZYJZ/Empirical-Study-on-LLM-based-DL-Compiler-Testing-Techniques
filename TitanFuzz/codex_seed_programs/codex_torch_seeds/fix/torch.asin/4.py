'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input data:\n', x)
print('Input data type:', x.type())
print('Input data size:', x.size())
y = torch.asin(x)
print('Output data:\n', y)
print('Output data type:', y.type())
print('Output data size:', y.size())