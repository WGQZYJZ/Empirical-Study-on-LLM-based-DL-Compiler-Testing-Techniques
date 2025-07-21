'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
a = torch.randn(2, 3, 4)
print(a)
(q, r) = torch.geqrf(a)
print(q)
print(r)