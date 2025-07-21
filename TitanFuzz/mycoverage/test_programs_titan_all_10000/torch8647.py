import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.cholesky_solve(b, A)
A = torch.rand(3, 3)
x = torch.cholesky_inverse(A)