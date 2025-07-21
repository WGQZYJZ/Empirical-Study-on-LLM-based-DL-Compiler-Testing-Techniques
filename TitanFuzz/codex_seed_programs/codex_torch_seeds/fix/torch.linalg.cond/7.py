'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
cond_A = torch.linalg.cond(A)
print(cond_A)