'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, 4)
print('Input: \n', x)
y = torch.floor(x)
print('Output: \n', y)