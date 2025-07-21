'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
import numpy as np
A = torch.randn(2, 2)
eigvals = torch.linalg.eigvals(A)
print(eigvals)
eigvals_np = np.linalg.eigvals(A.numpy())
print(eigvals_np)
eigvals_np = np.linalg.eigvals(A.numpy())
print(eigvals_np)
eigvals_np = np.linalg.eigvals(A.numpy())
print(eigvals_np)
eigvals_np = np.linalg.eigvals(A.numpy())
print(eigvals_np)
eigvals_np = np.linalg.eigvals(A.numpy())