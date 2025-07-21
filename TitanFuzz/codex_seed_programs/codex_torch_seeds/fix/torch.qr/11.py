'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 4)
print('Input: \n', input)
print('Task 3: Call the API torch.qr')
(q, r) = torch.qr(input)
print('Q: \n', q)
print('R: \n', r)