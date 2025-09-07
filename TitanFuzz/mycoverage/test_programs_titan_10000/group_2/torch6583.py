import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(4, 4)
k = 2
dim = 0
keepdim = False
output = torch.kthvalue(input, k, dim, keepdim)