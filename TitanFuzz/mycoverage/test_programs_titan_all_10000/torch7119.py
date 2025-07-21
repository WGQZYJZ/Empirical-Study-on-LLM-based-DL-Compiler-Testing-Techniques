import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.renorm(input, p=2, dim=1, maxnorm=1)