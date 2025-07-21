'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
'\nTask 2: Generate input data\n'
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
'\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
cond_A = torch.linalg.cond(A)
print('The condition number of A is: ', cond_A)