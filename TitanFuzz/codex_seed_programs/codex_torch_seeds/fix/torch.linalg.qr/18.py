"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(3, 3)
(q, r) = torch.linalg.qr(A)
print(q.shape, r.shape)
print(torch.matmul(q, r))
print(A)
print(torch.matmul(q, q.transpose(1, 0)))
print(r)
print(torch.matmul(q.transpose(1, 0), q))
print(torch.matmul(q.conj(), q.transpose(1, 0)))