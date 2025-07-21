"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
import numpy as np
A = torch.randn(3, 3)
print(A)
A = (A @ A.t())
print(A)
(e, v) = torch.linalg.eigh(A)
print(e)
print(v)
"\nTask 4: Call the API torch.linalg.eig\ntorch.linalg.eig(A, UPLO='L', *, out=None)\n"
(e, v) = torch.linalg.eig(A)
print(e)
print(v)
"\nTask 5: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, UPLO='L', *, out=None)\n"
e = torch.linalg.eigvals(A)
print(e)