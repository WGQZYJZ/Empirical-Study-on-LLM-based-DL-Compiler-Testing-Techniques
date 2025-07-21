'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
print(A)
print(torch.linalg.matrix_power(A, 3))