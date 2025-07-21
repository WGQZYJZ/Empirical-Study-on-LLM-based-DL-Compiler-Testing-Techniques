'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 5)
A_pinv = torch.linalg.pinv(A)
print(A)
print(A_pinv)