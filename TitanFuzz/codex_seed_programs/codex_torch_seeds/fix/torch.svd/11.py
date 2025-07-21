'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
A = torch.rand(3, 3)
print('A:', A)
(U, S, V) = torch.svd(A)
print('U:', U)
print('S:', S)
print('V:', V)