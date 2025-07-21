'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
import torch
A = torch.rand(10, 10)
cond_value = torch.linalg.cond(A, p=None, out=None)
print(cond_value)