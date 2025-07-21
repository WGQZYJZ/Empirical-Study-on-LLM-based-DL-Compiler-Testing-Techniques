'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
import torch
A = torch.rand(2, 2, requires_grad=True)
B = torch.rand(2, 2, requires_grad=True)
print(A)
print(B)
C = torch.linalg.solve(A, B)
print(C)
D = torch.linalg.solve(A, B, out=None)
print(D)