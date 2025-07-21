'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
x = torch.rand(3, 5)
y = torch.rand(3, 5)
print(torch.less(x, y))
print(torch.less_equal(x, y))