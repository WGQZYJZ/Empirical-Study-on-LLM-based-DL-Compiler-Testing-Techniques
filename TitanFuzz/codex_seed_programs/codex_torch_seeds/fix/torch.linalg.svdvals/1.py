'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svdvals\ntorch.linalg.svdvals(A, *, out=None)\n'
import torch
A = torch.randn(4, 4)
print(A)
s = torch.linalg.svdvals(A)
print(s)
print(torch.linalg.svdvals(torch.randn(4, 4)))
print(torch.linalg.svdvals(torch.randn(4, 4, 4)))
print(torch.linalg.svdvals(torch.randn(4, 4, 4, 4)))