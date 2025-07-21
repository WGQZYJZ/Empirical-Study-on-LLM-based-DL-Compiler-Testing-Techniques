'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svdvals\ntorch.linalg.svdvals(A, *, out=None)\n'
import torch
A = torch.randn(4, 4)
print('A is: ', A)
s = torch.linalg.svdvals(A)
print('s is: ', s)