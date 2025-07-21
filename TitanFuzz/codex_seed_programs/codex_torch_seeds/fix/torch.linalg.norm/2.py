'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
A = torch.rand(2, 3)
print('A:', A)
print('norm of A:', torch.linalg.norm(A))
print('norm of a vector:', torch.linalg.norm(A[0]))
print('norm of a matrix row:', torch.linalg.norm(A, dim=1))
print('norm of a matrix column:', torch.linalg.norm(A, dim=0))
print('norm of a matrix row with keepdim:', torch.linalg.norm(A, dim=1, keepdim=True))
print('norm of a matrix column with keepdim:', torch.linalg.norm(A, dim=0, keepdim=True))