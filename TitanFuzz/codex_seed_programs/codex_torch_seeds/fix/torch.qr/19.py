'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
x = torch.randn(4, 4)
print('Input data: ', x)
print('\nTask 3: Call the API torch.qr')
(q, r) = torch.qr(x)
print('Q: ', q)
print('R: ', r)