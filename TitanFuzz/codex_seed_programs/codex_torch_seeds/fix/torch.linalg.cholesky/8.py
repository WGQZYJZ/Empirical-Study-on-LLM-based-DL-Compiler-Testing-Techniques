'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.randn(2, 2)
A_t = A.t()
A_sym = torch.matmul(A_t, A)
print('A_sym: ', A_sym)
L_sym = torch.linalg.cholesky(A_sym, upper=False)
print('L_sym: ', L_sym)