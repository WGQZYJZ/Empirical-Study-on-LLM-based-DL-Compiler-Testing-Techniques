'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
A = torch.rand(2, 3)
print(A)
print(torch.linalg.norm(A, ord=None, dim=None, keepdim=False, out=None, dtype=None))
print(torch.norm(A, p=None, dim=None, keepdim=False, out=None, dtype=None))
print(torch.norm(A, p=2, dim=None, keepdim=False, out=None, dtype=None))
print(torch.norm(A, p=2, dim=1, keepdim=False, out=None, dtype=None))
print(torch.norm(A, p=2, dim=1, keepdim=True, out=None, dtype=None))