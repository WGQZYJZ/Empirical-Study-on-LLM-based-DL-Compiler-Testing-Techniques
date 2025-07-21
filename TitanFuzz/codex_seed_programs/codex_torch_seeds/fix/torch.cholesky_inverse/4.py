'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
import numpy as np
A = torch.randn(3, 3)
A = torch.mm(A.t(), A)
B = torch.cholesky_inverse(A)
print(B)