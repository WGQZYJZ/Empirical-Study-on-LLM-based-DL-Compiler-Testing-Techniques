'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
A = torch.randn(4, 4)
B = torch.randn(4, 4)
C = torch.linalg.matmul(A, B)
print(C)
D = torch.matmul(A, B)
print(D)
E = torch.mm(A, B)
print(E)