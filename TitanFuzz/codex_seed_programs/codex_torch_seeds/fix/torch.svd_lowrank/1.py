'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd_lowrank\ntorch.svd_lowrank(A, q=6, niter=2, M=None)\n'
import torch
A = torch.randn(8, 8)
print(A)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
print('U:', U)
print('S:', S)
print('V:', V)