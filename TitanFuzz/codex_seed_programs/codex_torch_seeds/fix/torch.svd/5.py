'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
import torch
A = torch.randn(3, 3)
(U, S, V) = torch.svd(A)
print(U)
print(S)
print(V)
print(torch.mm(U, torch.mm(torch.diag(S), V.t())))
print((torch.mm(U, torch.mm(torch.diag(S), V.t())) - A))