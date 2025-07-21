"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
A = torch.rand(2, 3)
print(A)
print(torch.linalg.matrix_norm(A, ord='fro', dim=((- 2), (- 1))))