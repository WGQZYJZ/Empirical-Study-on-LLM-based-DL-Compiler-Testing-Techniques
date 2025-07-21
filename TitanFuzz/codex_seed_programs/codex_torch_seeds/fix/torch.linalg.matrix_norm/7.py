"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
import torch
A = torch.randn(2, 3, 5)
torch.linalg.matrix_norm(A, ord='fro', dim=((- 2), (- 1)), keepdim=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
import torch
A = torch.randn(2, 3, 5)
n = 3