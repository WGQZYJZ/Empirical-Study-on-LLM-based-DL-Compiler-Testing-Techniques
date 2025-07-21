'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input data: ', x)
y = torch.special.logsumexp(x, dim=1, keepdim=True)
print('Output data: ', y)