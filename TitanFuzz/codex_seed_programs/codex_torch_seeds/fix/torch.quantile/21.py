'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
x = torch.randn((2, 4))
print('x = \n', x)
print('x.shape = ', x.shape)
q = torch.quantile(x, 0.5, dim=1, keepdim=True)
print('q = \n', q)
print('q.shape = ', q.shape)
y = torch.quantile(x, 0.5, dim=1, keepdim=False)
print('y = \n', y)
print('y.shape = ', y.shape)