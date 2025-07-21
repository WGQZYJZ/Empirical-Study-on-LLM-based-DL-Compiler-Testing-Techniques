'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float)
out = torch.digamma(input)
print(out)