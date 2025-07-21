'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print('A = \n', A)
cond_A = torch.linalg.cond(A)
print('cond_A = \n', cond_A)