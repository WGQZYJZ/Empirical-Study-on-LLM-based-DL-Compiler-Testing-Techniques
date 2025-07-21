'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
(sign, logdet) = torch.linalg.slogdet(A)
print(sign)
print(logdet)
A = torch.randn(4, 4)
print(A)
(sign, logdet) = torch.linalg.slogdet(A)
print(sign)
print(logdet)