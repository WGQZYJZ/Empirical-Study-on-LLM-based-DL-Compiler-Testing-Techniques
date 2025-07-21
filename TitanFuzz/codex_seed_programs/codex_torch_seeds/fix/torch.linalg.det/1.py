'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
A = torch.randn(2, 2)
print('A = ', A)
B = torch.linalg.det(A)
print('B = ', B)