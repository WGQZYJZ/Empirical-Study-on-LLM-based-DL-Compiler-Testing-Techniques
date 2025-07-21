import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, requires_grad=True)
mat = torch.randn(10, 10)
vec = torch.randn(10)
y = torch.addmv(x, mat, vec)
y.backward(torch.ones(10))
x = torch.randn(10, requires_grad=True)
mat = torch.randn(10, 10)
vec = torch.randn(10)
y = torch.addmv(x, mat, vec, alpha=0.5)
y.backward(torch.ones(10))