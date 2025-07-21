'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd_lowrank\ntorch.svd_lowrank(A, q=6, niter=2, M=None)\n'
import torch
A = torch.randn(10, 10)
(u, s, v) = torch.svd_lowrank(A, q=6, niter=2, M=None)
print(u)
print(s)
print(v)