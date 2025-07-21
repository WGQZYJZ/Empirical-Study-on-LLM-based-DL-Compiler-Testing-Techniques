'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.Tensor([[1, 2], [3, 4]])
print(torch.linalg.matrix_power(A, 3))
A = torch.Tensor([[1, 2], [3, 4]])
print(torch.linalg.matrix_power(A, 3, out=A))