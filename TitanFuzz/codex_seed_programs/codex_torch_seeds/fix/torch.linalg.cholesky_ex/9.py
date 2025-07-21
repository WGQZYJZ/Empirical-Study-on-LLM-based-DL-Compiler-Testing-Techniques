'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[2, 1, 1], [1, 2, 1], [1, 1, 2]], dtype=torch.float)
L = torch.linalg.cholesky_ex(A, upper=False)
print(L)
L = torch.linalg.cholesky_ex(A, upper=True)
print(L)