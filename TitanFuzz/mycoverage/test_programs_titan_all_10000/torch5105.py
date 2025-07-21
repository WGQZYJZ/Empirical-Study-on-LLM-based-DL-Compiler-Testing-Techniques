import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A = (A.t() @ A)
b = torch.randn(3, 1)
x = torch.cholesky_solve(b, A)