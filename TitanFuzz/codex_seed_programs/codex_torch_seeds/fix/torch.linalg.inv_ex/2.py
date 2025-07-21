'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv_ex\ntorch.linalg.inv_ex(A, *, check_errors=False, out=None)\n'
import torch
A = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
invA = torch.linalg.inv_ex(A)
print(invA)