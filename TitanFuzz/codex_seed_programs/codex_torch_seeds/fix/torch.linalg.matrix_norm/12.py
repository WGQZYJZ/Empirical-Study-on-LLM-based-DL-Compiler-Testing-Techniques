"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
A = torch.randn(3, 3)
print(A)
print(torch.linalg.matrix_norm(A, ord=2))
print(torch.linalg.matrix_norm(A, ord=2, dim=((- 2), (- 1))))
print(torch.linalg.matrix_norm(A, ord=2, dim=((- 2), (- 1)), keepdim=True))
print(torch.linalg.matrix_norm(A, ord=2, dim=((- 2), (- 1)), keepdim=True).shape)
print(torch.linalg.matrix_norm(A, ord=2, dim=((- 2), (- 1)), keepdim=False))
print(torch.linalg.matrix_norm(A, ord=2, dim=((- 2), (- 1)), keepdim=False).shape)