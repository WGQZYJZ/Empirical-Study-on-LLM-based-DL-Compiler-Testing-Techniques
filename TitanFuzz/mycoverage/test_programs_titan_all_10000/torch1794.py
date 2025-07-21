import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
q = 0.5
dim = 0
keepdim = False
quantile = torch.quantile(input, q, dim, keepdim)