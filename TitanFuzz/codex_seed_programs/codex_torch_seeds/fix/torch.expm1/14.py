'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float)
print(input)
out = torch.expm1(input)
print(out)