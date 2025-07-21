'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmv\ntorch.addmv(input, mat, vec, *, beta=1, alpha=1, out=None)\n'
import torch
from torch import autograd
import numpy as np
x = torch.randn(10, requires_grad=True)
mat = torch.randn(10, 10)
vec = torch.randn(10)
y = torch.addmv(x, mat, vec)
print(y)
y.backward(torch.ones(10))
print(x.grad)
x = torch.randn(10, requires_grad=True)
mat = torch.randn(10, 10)
vec = torch.randn(10)
y = torch.addmv(x, mat, vec, alpha=0.5)
print(y)
y.backward(torch.ones(10))
print(x.grad)