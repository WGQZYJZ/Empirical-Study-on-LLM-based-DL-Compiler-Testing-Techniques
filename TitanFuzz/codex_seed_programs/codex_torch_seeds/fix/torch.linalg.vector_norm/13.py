'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.vector_norm\ntorch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
A = torch.randn(4, 3)
print(A)
print(torch.linalg.vector_norm(A, ord=2, dim=1, keepdim=False))
print(torch.linalg.vector_norm(A, ord=2, dim=1, keepdim=True))
print(torch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False))
print(torch.linalg.vector_norm(A, ord=2, dim=None, keepdim=True))