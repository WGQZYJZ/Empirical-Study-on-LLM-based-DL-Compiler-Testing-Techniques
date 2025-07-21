'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
import numpy as np
import torch
x = torch.randn(5, 5)
print(x)
y = torch.special.logit(x)
print(y)
z = torch.special.expit(y)
print(z)
w = torch.sigmoid(x)
print(w)
v = torch.logit(w)
print(v)