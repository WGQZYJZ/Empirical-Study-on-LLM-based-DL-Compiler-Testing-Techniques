'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd_lowrank\ntorch.svd_lowrank(A, q=6, niter=2, M=None)\n'
import torch
import numpy as np
A = torch.randn(10, 10)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
print(U)
print(S)
print(V)
print(U.shape)
print(S.shape)
print(V.shape)