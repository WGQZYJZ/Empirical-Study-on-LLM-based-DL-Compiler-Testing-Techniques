'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
print(torch.linalg.norm(A))
print(torch.linalg.norm(A, 1))
print(torch.linalg.norm(A, 2))
print(torch.linalg.norm(A, float('inf')))
print(torch.linalg.norm(A, 1, 0))
print(torch.linalg.norm(A, 1, 1))
print(torch.linalg.norm(A, 2, 0))
print(torch.linalg.norm(A, 2, 1))
print(torch.linalg.norm(A, float('inf'), 0))
print(torch.linalg.norm(A, float('inf'), 1))