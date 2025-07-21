'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_rank\ntorch.matrix_rank(input, tol=None, symmetric=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(torch.matrix_rank(input))