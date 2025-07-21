'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.randn(5, 5)
A_inv = torch.linalg.inv(A)
print('A_inv = {}'.format(A_inv))
print('A_inv * A = {}'.format(A_inv.mm(A)))