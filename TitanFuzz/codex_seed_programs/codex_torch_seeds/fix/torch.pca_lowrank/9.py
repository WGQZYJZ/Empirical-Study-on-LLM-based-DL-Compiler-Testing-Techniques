'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
import numpy as np
(n, d, r) = (1000, 10, 5)
A = torch.randn(n, d, dtype=torch.float64)
q = torch.pca_lowrank(A, q=r, center=True, niter=2)
print(q)