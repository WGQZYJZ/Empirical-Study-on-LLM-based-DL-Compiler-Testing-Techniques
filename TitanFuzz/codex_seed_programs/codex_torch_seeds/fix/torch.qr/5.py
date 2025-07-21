'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 5)
(q, r) = torch.qr(input)
print(q)
print(r)
print(q.mm(r))