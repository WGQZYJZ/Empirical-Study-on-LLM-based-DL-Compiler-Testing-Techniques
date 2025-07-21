'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
A = torch.rand(4, 4)
cond_A = torch.linalg.cond(A)
print('The condition number of A is: ', cond_A)