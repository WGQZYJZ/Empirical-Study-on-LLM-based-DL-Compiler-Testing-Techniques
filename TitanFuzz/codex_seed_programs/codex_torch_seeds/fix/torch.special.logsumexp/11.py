'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
print(x)
y = torch.special.logsumexp(x, dim=1, keepdim=True)
print(y)
y = torch.logsumexp(x, dim=1, keepdim=True)
print(y)
y = torch.max(x, dim=1, keepdim=True)
print(y)