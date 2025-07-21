'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input data: \n', input)
(q, r) = torch.qr(input)
print('Q matrix: \n', q)
print('R matrix: \n', r)