'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.vector_norm\ntorch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
print(torch.linalg.vector_norm(A))
print(torch.linalg.vector_norm(A, ord=1))
print(torch.linalg.vector_norm(A, ord=2))
print(torch.linalg.vector_norm(A, ord=3))
print(torch.linalg.vector_norm(A, ord=4))
print(torch.linalg.vector_norm(A, ord=5))
print(torch.linalg.vector_norm(A, ord=6))
print(torch.linalg.vector_norm(A, ord=7))
print(torch.linalg.vector_norm(A, ord=8))
print(torch.linalg.vector_norm(A, ord=9))