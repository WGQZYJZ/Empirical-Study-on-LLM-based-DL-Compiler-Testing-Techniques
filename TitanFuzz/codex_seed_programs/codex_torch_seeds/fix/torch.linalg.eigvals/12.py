'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print('Input data A: \n', A)
eigvals = torch.linalg.eigvals(A)
print('eigenvalues: \n', eigvals)