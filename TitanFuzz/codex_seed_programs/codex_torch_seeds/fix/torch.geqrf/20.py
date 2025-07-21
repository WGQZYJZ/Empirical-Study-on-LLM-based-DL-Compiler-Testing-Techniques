'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
input = torch.randn(5, 5)
(q, r) = torch.geqrf(input)
print(q)
print(r)