'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv_ex\ntorch.linalg.inv_ex(A, *, check_errors=False, out=None)\n'
import torch
import numpy as np
A = torch.randn(3, 3)
print(A)
A_inv = torch.linalg.inv_ex(A)
print(A_inv)
A_inv_np = np.linalg.inv(A.numpy())
print(A_inv_np)