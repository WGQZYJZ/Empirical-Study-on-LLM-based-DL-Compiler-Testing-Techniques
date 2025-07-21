'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_rank\ntorch.linalg.matrix_rank(A, tol=None, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(5, 5)
rank = torch.linalg.matrix_rank(A)
print(rank)