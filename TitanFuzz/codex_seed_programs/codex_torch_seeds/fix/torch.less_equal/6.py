'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
print('x = ', x)
print('y = ', y)
out = torch.less_equal(x, y)
print('out = ', out)