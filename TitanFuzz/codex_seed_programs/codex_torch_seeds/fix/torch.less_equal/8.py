'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
print(x)
print(y)
print(torch.less_equal(x, y))
print(torch.less_equal(x, x))