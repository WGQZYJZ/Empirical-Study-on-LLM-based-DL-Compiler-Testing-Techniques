'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
A = torch.randn(4, 4)
(U, S, V) = torch.svd(A)
print(U.shape, S.shape, V.shape)
print(U, S, V)