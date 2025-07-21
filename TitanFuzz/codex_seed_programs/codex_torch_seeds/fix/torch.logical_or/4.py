'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_or\ntorch.logical_or(input, other, *, out=None)\n'
import torch
a = torch.tensor([False, True, False, True])
b = torch.tensor([False, False, True, True])
c = torch.logical_or(a, b)
print(c)
d = (a | b)
print(d)