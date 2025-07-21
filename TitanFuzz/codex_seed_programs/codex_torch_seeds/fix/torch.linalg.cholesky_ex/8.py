'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.randn(3, 3)
A_t = A.t()
A_symm = torch.matmul(A_t, A)
L = torch.linalg.cholesky_ex(A_symm)
print(L)