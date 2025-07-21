"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
A = torch.randn(3, 3)
print(A)
B = torch.linalg.matrix_norm(A, ord='fro')
print(B)
C = torch.linalg.matrix_norm(A, ord=2)
print(C)
D = torch.linalg.matrix_norm(A, ord=1)
print(D)
E = torch.linalg.matrix_norm(A, ord=float('inf'))
print(E)