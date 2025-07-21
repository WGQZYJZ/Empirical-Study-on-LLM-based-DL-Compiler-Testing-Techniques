'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
input = torch.randn(5, 3, dtype=torch.float)
(u, s, v) = torch.svd(input)
print(u.shape, s.shape, v.shape)
print(u)
print(s)
print(v)