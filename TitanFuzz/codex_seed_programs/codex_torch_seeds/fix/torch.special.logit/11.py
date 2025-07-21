'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, requires_grad=True)
y = torch.special.logit(x)
print(y)
z = torch.special.expit(y)
print(z)