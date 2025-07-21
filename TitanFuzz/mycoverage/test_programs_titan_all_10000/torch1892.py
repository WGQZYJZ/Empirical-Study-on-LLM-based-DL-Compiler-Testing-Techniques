import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
b = torch.randn(3, 3)
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)[0]