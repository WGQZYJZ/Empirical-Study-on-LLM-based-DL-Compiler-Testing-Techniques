"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
print(torch.__version__)
A = torch.randn(2, 3)
print(A)
(q, r) = torch.linalg.qr(A)
print(q)
print(r)
(q, r) = torch.linalg.qr(A, out=(torch.empty(2, 3), torch.empty(2, 3)))
print(q)
print(r)