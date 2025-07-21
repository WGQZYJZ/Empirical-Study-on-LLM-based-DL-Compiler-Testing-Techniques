'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.randn(2, 2)
A = (A.t() @ A)
print('A:')
print(A)
print('\ncholesky:')
print(torch.linalg.cholesky_ex(A))