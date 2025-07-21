'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
(q, r) = torch.geqrf(input)
print('Q: ', q)
print('R: ', r)