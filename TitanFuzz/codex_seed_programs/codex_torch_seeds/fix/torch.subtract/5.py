'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.subtract(a, b)
print(c)