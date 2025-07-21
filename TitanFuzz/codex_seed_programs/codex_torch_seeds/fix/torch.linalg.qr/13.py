"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = torch.randn(4, 4)
print('Task 3: Call the API torch.linalg.qr')
(Q, R) = torch.linalg.qr(A)
print('Q: ', Q)
print('R: ', R)