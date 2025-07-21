'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
A = torch.randn(5, 5)
B = torch.randn(5, 5)
C = torch.randn(5, 5)
D = torch.randn(5, 5)
E = torch.randn(5, 5)
print(torch.linalg.multi_dot([A, B, C, D, E]))