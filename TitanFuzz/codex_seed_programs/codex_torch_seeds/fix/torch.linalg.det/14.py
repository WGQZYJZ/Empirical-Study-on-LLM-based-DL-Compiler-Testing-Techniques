'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print('A:\n', A)
print('torch.linalg.det(A):\n', torch.linalg.det(A))