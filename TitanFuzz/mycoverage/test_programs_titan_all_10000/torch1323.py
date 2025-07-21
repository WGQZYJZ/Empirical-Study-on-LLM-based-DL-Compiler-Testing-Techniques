import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
k = 2
dim = 1
keepdim = True
(value, index) = torch.kthvalue(input, k, dim, keepdim)