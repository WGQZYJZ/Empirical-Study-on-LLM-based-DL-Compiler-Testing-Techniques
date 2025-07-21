"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(8, 8)
A = A.mm(A.t())
print(A)
(e, v) = torch.linalg.eigh(A)
print(e)
print(v)