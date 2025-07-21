'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
import numpy as np
import torch
A = np.random.rand(5, 5)
A = torch.tensor(A)
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)
print(U.shape)
print(S.shape)
print(V.shape)