'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
A = torch.randn(3, 3, requires_grad=True)
B = torch.randn(3, 3, requires_grad=True)
C = torch.randn(3, 3, requires_grad=True)
D = torch.linalg.multi_dot([A, B, C])
print(D)