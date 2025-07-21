'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
A = torch.randn(3, 3)
cond_A = torch.linalg.cond(A)
print('cond_A=', cond_A)