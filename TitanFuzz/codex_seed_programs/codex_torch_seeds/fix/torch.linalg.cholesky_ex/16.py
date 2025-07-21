'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [2, 3, 4], [3, 4, 5]], dtype=torch.float32)
L = torch.linalg.cholesky_ex(A)
print('A: ', A)
print('L: ', L)