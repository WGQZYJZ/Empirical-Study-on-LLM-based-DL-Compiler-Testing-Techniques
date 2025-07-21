"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(3, 5)
(Q, R) = torch.linalg.qr(A)
print(Q.matmul(R))
print(A)