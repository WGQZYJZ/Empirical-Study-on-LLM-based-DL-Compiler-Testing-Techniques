'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
A_inv = torch.linalg.inv(A)
print('A = \n', A)
print('A_inv = \n', A_inv)
print('A_inv * A = \n', A_inv.mm(A))