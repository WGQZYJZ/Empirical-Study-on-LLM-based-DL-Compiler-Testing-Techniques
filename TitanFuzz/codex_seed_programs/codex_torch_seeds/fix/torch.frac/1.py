'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.frac(x))
print(torch.frac(x, out=torch.empty_like(x)))