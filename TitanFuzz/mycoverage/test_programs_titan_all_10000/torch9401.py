import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 5)
output = torch.renorm(input, p=1, dim=0, maxnorm=1)