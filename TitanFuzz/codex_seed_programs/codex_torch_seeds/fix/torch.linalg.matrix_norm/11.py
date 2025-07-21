"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
A = torch.randn(10, 10)
B = torch.randn(10, 10, 10)
print(torch.linalg.matrix_norm(A, ord='fro'))
print(torch.linalg.matrix_norm(B, ord='fro'))