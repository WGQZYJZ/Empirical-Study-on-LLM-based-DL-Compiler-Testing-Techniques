'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('The input data is: ', x)
y = torch.arccos(x)
print('The result of torch.arccos is: ', y)