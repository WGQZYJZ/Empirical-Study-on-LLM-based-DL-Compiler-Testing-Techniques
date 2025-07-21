'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
A = torch.randn(3, 3)
A = torch.matmul(A, A.t())
A_inv = torch.cholesky_inverse(A)
print(A_inv)