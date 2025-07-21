'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input_data = torch.randn(3, 5)
print('Input data is: \n', input_data)
(q, r) = torch.qr(input_data)
print('Q is: \n', q)
print('R is: \n', r)