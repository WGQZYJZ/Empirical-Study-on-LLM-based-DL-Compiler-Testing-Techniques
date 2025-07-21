"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.rand(10, 10)
A = A.mm(A.t())
(eig_vals, eig_vecs) = torch.linalg.eigh(A)
print(eig_vals)
print(eig_vecs)