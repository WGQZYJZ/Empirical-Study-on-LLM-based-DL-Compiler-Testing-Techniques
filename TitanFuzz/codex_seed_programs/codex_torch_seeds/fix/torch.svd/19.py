'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
(u, s, v) = torch.svd(input)
print('Input: ', input)
print('U: ', u)
print('S: ', s)
print('V: ', v)