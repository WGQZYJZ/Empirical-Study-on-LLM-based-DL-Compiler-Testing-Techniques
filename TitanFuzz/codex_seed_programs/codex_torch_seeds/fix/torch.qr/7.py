'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
import torch
input_data = torch.randn(3, 5)
print('input_data:', input_data)
(q, r) = torch.qr(input_data)
print('q:', q)
print('r:', r)