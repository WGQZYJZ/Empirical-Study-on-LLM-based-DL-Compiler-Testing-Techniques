import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 3)
a = (a @ a.t())
b = torch.randn(3, 2)
x = torch.cholesky_solve(b, a)