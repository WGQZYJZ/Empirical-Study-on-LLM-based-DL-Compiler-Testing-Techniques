"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.rand(3, 4, dtype=torch.float, requires_grad=True)
print(A)
(q, r) = torch.linalg.qr(A)
print(q)
print(r)