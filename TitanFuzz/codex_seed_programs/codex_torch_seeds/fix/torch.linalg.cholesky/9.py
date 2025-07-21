'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.rand(4, 4)
A = torch.mm(A.t(), A)
print('A:', A)
L = torch.linalg.cholesky(A)
print('L:', L)
print('A - L.t().mm(L):', (A - L.t().mm(L)))