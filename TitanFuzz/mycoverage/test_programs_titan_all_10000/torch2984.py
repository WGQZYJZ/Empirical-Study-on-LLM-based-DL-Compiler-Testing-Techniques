import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 2)
b = torch.renorm(a, p=2, dim=1, maxnorm=1)