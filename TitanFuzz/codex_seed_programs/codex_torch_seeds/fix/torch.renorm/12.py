'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
import torch
tensor = torch.randn(3, 5)
tensor = torch.renorm(tensor, p=2, dim=1, maxnorm=1)
print(tensor)