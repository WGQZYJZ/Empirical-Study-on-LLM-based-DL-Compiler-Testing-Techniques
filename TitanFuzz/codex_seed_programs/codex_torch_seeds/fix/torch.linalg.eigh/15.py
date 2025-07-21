"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = torch.rand(5, 5)
print('Task 3: Call the API torch.linalg.eigh')
(eigvals, eigvecs) = torch.linalg.eigh(A)
print('eigvals:', eigvals)
print('eigvecs:', eigvecs)