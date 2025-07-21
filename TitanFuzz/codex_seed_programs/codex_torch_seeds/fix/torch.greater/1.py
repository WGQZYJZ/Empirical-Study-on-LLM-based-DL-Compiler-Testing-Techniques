'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
a = torch.randn(1, 3)
b = torch.randn(1, 3)
c = torch.greater(a, b)
print(c)