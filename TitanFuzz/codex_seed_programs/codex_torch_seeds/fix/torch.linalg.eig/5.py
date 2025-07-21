'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
(eig_vals, eig_vecs) = torch.linalg.eig(A)
print('Eigenvalues:', eig_vals)
print('Eigenvectors:', eig_vecs)