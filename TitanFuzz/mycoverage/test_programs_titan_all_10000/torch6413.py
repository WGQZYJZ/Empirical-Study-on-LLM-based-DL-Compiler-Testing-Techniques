import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 3), requires_grad=True)
output = torch.cholesky_inverse(input)