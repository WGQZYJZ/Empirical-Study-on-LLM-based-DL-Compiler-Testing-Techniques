'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
a = torch.randn(3, 3)
a = ((a * 3) / (a - 1))
print('a:', a)
(q, r) = torch.geqrf(a)
print('q:', q)
print('r:', r)