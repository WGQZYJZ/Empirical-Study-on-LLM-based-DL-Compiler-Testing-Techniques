'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
a = torch.randn(3, 3)
(e, v) = torch.eig(a, True)
print(e)
print(v)
(e, v) = torch.eig(a, True)
print(e)
print(v)