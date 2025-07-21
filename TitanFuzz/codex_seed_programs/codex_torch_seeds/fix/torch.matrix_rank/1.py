'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_rank\ntorch.matrix_rank(input, tol=None, symmetric=False, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
print(torch.matrix_rank(x))