"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
import torch
A = torch.rand(3, 3)
(q, r) = torch.linalg.qr(A)
print('A:', A)
print('q:', q)
print('r:', r)
print('q * r:', torch.mm(q, r))
print('q.t * q:', torch.mm(q.t(), q))
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='complete', *, out=None)\n"
import torch
import torch
A = torch.rand(3, 3)