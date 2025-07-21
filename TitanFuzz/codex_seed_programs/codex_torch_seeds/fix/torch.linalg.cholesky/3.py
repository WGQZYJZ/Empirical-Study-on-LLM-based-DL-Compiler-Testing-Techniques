'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.randn(3, 3)
A = A.mm(A.t())
print('A is: ', A)
L = torch.linalg.cholesky(A, upper=False)
print('L is: ', L)