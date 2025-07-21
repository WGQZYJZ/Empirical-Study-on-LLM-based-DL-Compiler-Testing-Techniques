'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
import torch
A = torch.rand(2, 3)
print(torch.linalg.norm(A, dim=1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
import torch
A = torch.rand(2, 3)
print(torch.linalg.norm(A, dim=1, keepdim=True))