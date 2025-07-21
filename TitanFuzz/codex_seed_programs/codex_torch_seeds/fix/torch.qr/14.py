'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
(q, r) = torch.qr(x)
print(q)
print(r)