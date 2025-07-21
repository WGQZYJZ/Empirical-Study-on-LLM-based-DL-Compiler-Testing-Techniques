'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
A = torch.rand(3, 3)
A = A.mm(A.t())
print(A)
L = torch.cholesky(A)
print(L)
print(L.mm(L.t()))