'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.randn(2, 2)
B = torch.linalg.matrix_power(A, 2)
print(B)