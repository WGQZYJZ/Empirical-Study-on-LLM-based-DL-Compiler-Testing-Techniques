"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(3, 4)
print('Input matrix A:', A)
(q, r) = torch.linalg.qr(A)
print('q:', q)
print('r:', r)
print('q*r:', torch.matmul(q, r))
print('q.t*q:', torch.matmul(q.t(), q))