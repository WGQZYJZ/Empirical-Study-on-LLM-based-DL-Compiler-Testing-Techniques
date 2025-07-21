'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
print(torch.less(a, b))
print(torch.less(a, 0.5))