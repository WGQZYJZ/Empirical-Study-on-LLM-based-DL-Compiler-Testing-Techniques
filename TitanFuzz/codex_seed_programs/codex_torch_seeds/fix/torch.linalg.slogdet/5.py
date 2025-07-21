'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
print(torch.linalg.slogdet(A))
print(torch.linalg.det(A))