'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater_equal\ntorch.greater_equal(input, other, *, out=None)\n'
import torch
a = torch.rand(3, 2)
b = torch.rand(3, 2)
c = torch.greater_equal(a, b)
print('Input 1: ', a)
print('Input 2: ', b)
print('Output: ', c)