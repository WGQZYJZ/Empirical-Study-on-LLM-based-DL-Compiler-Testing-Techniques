'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 2, 3])
c = torch.le(a, b)
print(c)