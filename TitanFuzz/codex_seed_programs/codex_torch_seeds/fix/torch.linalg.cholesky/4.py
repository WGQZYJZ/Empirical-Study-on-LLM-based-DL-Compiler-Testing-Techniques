'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
cholesky = torch.linalg.cholesky(A)
print(cholesky)