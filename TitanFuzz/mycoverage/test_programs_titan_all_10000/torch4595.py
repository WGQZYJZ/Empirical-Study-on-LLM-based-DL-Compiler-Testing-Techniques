import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
input
torch.renorm(input, p=2, dim=0, maxnorm=1)
torch.renorm(input, p=2, dim=1, maxnorm=1)