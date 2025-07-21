'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
a = torch.randn(1, 3)
print(a)
print(torch.atan(a))