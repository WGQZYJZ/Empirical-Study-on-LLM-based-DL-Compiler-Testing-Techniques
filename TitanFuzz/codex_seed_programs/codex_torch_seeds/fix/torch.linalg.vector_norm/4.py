'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.vector_norm\ntorch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
A = torch.randn(10, 3, 5)
print('A: ', A)
result = torch.linalg.vector_norm(A, dim=1)
print('result: ', result)