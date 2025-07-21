'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
(q, r) = torch.qr(input_data)
print('Q: ', q)
print('R: ', r)