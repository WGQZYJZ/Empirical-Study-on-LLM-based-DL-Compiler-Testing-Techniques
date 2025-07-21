"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(3, 3)
print(A)
(Q, R) = torch.linalg.qr(A)
print(Q)
print(R)
print(Q.matmul(R))
print(Q.t().matmul(Q))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, some=True, compute_uv=True, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
(U, S, V) = torch.linalg.svd(A)
print(U)
print(S)
print(V)
print(U.matmul(torch.diag(S)).matmul(V.t()))