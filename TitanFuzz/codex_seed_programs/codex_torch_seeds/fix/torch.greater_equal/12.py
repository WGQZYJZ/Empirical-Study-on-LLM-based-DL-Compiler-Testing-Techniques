'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater_equal\ntorch.greater_equal(input, other, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('x: \n', x)
y = torch.greater_equal(x, 0)
print('y: \n', y)