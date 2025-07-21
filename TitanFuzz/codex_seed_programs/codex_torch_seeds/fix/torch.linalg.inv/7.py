'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.randn(3, 3, requires_grad=True)
print(A)
A_inv = torch.linalg.inv(A)
print(A_inv)