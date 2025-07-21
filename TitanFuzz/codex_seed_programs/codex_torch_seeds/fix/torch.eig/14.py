'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
A = torch.randn(3, 3)
(e, v) = torch.eig(A, eigenvectors=True)
print('Eigenvalues: ', e)
print('Eigenvectors: ', v)
(u, s, v) = torch.svd(A, some=True)
print('U: ', u)
print('S: ', s)
print('V: ', v)