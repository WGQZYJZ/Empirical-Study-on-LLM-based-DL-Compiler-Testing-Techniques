'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
A = torch.rand(10, 20)
A = torch.rand(10, 20)
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)
print('U: ', U)
print('S: ', S)
print('V: ', V)
print('U: ', U.shape)
print('S: ', S.shape)
print('V: ', V.shape)