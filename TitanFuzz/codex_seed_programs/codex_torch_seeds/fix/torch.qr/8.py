'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
(q, r) = torch.qr(input)
print(q)
print(r)
print(q.matmul(r))
print(torch.qr(input, some=True))