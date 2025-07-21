'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, full_matrices=True, *, out=None)\n'
import torch
A = torch.randn(4, 4)
(U, S, V) = torch.linalg.svd(A)
print(U)
print(S)
print(V)