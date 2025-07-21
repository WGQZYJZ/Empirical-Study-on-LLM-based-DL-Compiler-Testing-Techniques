'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
import torch
x = torch.randn(4, 4)
y = torch.renorm(x, p=2, dim=1, maxnorm=1)
print(x)
print(y)