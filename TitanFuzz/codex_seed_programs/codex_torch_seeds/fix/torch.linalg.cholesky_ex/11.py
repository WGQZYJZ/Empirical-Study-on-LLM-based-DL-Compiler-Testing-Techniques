'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
import torch
A = torch.randn((5, 5))
A = torch.mm(A, A.t())
L = torch.linalg.cholesky_ex(A, upper=False)
print(L)