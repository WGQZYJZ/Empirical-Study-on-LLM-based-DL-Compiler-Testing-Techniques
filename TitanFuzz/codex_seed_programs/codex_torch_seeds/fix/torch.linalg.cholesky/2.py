'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.randn(2, 2)
A_t = A.t()
A_symm = torch.matmul(A, A_t)
print('A = ', A)
print('A_t = ', A_t)
print('A_symm = ', A_symm)
L = torch.linalg.cholesky(A_symm, upper=False)
print('L = ', L)
print('L * L.t() = ', torch.matmul(L, L.t()))