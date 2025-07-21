'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
A = torch.randn(3, 5)
A[0, :] = A[1, :]
A[2, :] = A[1, :]
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)
print('U = ', U)
print('S = ', S)
print('V = ', V)