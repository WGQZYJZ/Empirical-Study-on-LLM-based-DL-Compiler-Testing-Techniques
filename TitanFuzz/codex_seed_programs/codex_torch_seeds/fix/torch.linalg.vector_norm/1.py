'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.vector_norm\ntorch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
print('\nTask 3: Call the API torch.linalg.vector_norm')
print(torch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, dtype=None, out=None))