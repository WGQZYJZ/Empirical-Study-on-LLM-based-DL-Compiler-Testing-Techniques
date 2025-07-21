'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.rand(2, 3)
print(A)
pinv_A = torch.linalg.pinv(A)
print(pinv_A)
pinv_A = torch.linalg.pinv(A, rcond=1e-15)
print(pinv_A)