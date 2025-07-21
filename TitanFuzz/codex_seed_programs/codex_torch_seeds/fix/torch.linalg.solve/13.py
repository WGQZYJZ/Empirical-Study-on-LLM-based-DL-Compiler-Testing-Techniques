'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
import torch
A = torch.rand(3, 3)
B = torch.rand(3, 3)
X = torch.linalg.solve(A, B)
print(X)
print(torch.matmul(A, X))