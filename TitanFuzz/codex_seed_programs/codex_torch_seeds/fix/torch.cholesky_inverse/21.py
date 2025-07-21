'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
import numpy as np
import torch
A = torch.rand(3, 3)
A = (A.t() @ A)
A = (A + torch.eye(3, 3))
A_np = A.numpy()
A_inv = torch.cholesky_inverse(A)
print(A_inv)
print(np.linalg.inv(A_np))