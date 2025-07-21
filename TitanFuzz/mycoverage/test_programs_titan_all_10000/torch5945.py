import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
input = input.mm(input.t())
result = torch.cholesky(input)
input = torch.randn(3, 3)
input = input.mm(input.t())
input2 = torch.randn(3, 3)
result = torch.cholesky_solve(input, input2)