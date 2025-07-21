'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(torch.sgn(x))