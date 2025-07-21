'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
a = torch.rand(4, 4)
b = torch.rand(4, 4)
print(torch.hypot(a, b))