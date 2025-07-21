'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(3, 5)
print('Input data: ', input_data)
print('Task 3: Call the API torch.qr')
(q, r) = torch.qr(input_data)
print('Q: ', q)
print('R: ', r)