'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [3.0, 6.0, 9.0]])
B = torch.linalg.cholesky_ex(A)
print(B)