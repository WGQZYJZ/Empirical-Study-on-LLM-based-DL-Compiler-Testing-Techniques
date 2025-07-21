'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
import numpy as np
A = torch.Tensor([[1, 2], [2, 1]])
print('A = ', A)
L = torch.linalg.cholesky_ex(A, upper=False)
print('L = ', L)
U = torch.linalg.cholesky_ex(A, upper=True)
print('U = ', U)