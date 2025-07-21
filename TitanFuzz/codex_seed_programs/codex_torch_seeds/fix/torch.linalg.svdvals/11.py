'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svdvals\ntorch.linalg.svdvals(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
s = torch.linalg.svdvals(A)
print('s = ', s)