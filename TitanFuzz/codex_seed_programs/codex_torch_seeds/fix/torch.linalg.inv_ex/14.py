'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv_ex\ntorch.linalg.inv_ex(A, *, check_errors=False, out=None)\n'
import torch
A = torch.rand(2, 2, dtype=torch.float64)
print(A)
A_inv = torch.linalg.inv_ex(A)
print(A_inv)