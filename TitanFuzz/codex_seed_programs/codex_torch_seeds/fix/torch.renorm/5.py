'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(torch.renorm(data, p=2, dim=1, maxnorm=1))
print(torch.renorm(data, p=2, dim=1, maxnorm=1, out=data))
print(data)