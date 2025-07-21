'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.randn(3, 3)
A = torch.matmul(A.t(), A)
print(torch.linalg.cholesky_ex(A))