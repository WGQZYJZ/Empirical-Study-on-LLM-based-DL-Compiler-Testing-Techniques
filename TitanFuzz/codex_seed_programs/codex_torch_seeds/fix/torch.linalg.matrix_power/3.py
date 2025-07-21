'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.rand(3, 3)
n = 2
print('A:\n', A)
print('n:\n', n)
print('torch.linalg.matrix_power(A, n):\n', torch.linalg.matrix_power(A, n))