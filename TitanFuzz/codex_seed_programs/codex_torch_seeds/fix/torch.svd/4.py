'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
(u, s, v) = torch.svd(input)
print('u: ', u)
print('s: ', s)
print('v: ', v)