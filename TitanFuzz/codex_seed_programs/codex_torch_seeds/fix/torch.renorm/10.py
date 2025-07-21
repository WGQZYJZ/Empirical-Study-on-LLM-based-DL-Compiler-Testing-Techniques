'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
print(input)
output = torch.renorm(input, p=2, dim=0, maxnorm=1)
print(output)