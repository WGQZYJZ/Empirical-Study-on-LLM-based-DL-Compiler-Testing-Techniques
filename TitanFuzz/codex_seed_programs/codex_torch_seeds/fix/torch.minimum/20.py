'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
c = torch.minimum(a, b)
print(c)