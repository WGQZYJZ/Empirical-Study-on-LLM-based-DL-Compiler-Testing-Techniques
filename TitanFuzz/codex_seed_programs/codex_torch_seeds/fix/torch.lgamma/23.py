'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input: ', x)
y = torch.lgamma(x)
print('Output: ', y)