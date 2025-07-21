'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input: ', x)
y = torch.abs(x)
print('Output: ', y)