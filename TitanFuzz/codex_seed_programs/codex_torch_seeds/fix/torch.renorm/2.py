'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
a = torch.randn(4, 2)
print('Input data: \n', a)
b = torch.renorm(a, p=2, dim=1, maxnorm=1)
print('Output data: \n', b)