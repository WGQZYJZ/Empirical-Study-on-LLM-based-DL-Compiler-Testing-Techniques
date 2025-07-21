'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, full_matrices=True, *, out=None)\n'
import torch
A = torch.randn(3, 2)
print('Input tensor: A = ', A)
(U, S, V) = torch.linalg.svd(A)
print('U = ', U)
print('S = ', S)
print('V = ', V)