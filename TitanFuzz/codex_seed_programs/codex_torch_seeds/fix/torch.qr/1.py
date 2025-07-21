'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
print('Input data: ', input)
(q, r) = torch.qr(input)
print('Q: ', q)
print('R: ', r)
print('Q*R: ', q.mm(r))
print('Q.T*Q: ', q.t().mm(q))
print('Q*Q.T: ', q.mm(q.t()))