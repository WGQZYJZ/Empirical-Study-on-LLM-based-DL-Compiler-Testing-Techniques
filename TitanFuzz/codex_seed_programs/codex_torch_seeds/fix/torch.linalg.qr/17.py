"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(2, 3)
print('Input: \n', A)
(Q, R) = torch.linalg.qr(A)
print('Q: \n', Q)
print('R: \n', R)