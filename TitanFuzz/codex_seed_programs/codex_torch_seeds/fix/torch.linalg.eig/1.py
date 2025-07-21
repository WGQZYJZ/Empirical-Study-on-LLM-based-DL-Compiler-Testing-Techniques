'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, *, out=None)\n'
import torch
a = torch.randn(3, 3)
a = torch.matmul(a, a.t())
(eig_vals, eig_vecs) = torch.linalg.eig(a)
print(eig_vals)
print(eig_vecs)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, *, out=None)\n'
import torch
a = torch.randn(3, 3)
a = torch.matmul(a, a.t())
(eig_vals, eig_vecs) = torch.linalg.eig(a)
print(eig_vals)
print(eig_vecs)