'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd_lowrank\ntorch.svd_lowrank(A, q=6, niter=2, M=None)\n'
import torch
A = torch.randn(10, 10)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
print(U.shape, S.shape, V.shape)
'\nTask 4: Call the API torch.svd\ntorch.svd(A, some=False, compute_uv=True, out=None)\n'
(U, S, V) = torch.svd(A, some=False, compute_uv=True, out=None)
print(U.shape, S.shape, V.shape)