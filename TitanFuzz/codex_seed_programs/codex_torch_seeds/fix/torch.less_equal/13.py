'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print(torch.less_equal(a, b))
print(torch.le(a, b))