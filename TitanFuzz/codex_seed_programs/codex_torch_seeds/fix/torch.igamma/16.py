'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igamma\ntorch.igamma(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
out = torch.igamma(input, other)
print(out)
print(out.dtype)
print(out.size())