'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
print(torch.linalg.inv(A))
print(torch.mm(A, torch.linalg.inv(A)))