'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = torch.rand(3, 3)
print('Task 3: Call the API torch.linalg.cond')
print(torch.linalg.cond(A))