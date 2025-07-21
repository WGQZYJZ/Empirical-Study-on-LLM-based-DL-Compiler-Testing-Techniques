"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A = A.mm(A.t())
(e, V) = torch.linalg.eigh(A)
print('A =', A)
print('e =', e)
print('V =', V)