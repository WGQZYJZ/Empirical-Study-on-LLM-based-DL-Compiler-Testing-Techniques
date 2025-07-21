'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv_ex\ntorch.linalg.inv_ex(A, *, check_errors=False, out=None)\n'
import torch
A = torch.rand(3, 3)
B = torch.linalg.inv_ex(A)
print(B)
C = torch.linalg.inv_ex(A, check_errors=True, out=None)
print(C)