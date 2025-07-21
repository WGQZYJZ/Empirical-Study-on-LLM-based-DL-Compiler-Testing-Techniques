'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
A = torch.rand(2, 3)
B = torch.rand(3, 2)
C = torch.rand(2, 2)
D = torch.rand(2, 2)
E = torch.rand(2, 2)
print(torch.linalg.multi_dot([A, B, C, D, E]))