'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
A = torch.randn(2, 2)
print('A = ', A)
eigvals = torch.linalg.eigvals(A)
print('eigvals = ', eigvals)