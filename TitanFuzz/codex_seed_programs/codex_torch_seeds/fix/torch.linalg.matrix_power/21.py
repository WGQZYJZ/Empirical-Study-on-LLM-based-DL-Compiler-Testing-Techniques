'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.rand(2, 2, dtype=torch.float32)
n = 2
out = torch.linalg.matrix_power(A, n)
print(out)