'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.vector_norm\ntorch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
A = torch.randn(4, 3)
print('A: ', A)
print('norm of A: ', torch.linalg.vector_norm(A))
print('norm of A along dim=1: ', torch.linalg.vector_norm(A, dim=1))
print('norm of A along dim=0: ', torch.linalg.vector_norm(A, dim=0))