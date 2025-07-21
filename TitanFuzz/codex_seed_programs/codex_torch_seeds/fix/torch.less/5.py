'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
t1 = torch.rand(2, 2)
t2 = torch.rand(2, 2)
less = torch.less(t1, t2)
print(less)
less_equal = torch.less_equal(t1, t2)
print(less_equal)