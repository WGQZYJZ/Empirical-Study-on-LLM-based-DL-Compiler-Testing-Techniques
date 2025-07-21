'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
inp = torch.randn(1, 2, 3)
print(inp)
print(torch.log1p(inp))