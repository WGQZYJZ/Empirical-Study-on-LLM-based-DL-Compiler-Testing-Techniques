'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
a = torch.randn(3, 3)
print(a)
(u, s, v) = torch.svd(a)
print(u)
print(s)
print(v)
print(u.mm(u.t()))
print(v.mm(v.t()))
print(u.mm(v.t()))
print(u.mm(torch.diag(s)).mm(v.t()))
print(s.dtype)