'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
import torch
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
n = 2
torch.linalg.matrix_power(A, n)
print(torch.linalg.matrix_power(A, n))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_rank\ntorch.linalg.matrix_rank(A, *, hermitian=False)\n'
import torch
import torch
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
torch.linalg.matrix_rank(A)