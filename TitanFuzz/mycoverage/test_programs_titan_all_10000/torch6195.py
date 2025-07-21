import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
torch.renorm(x, p=2, dim=0, maxnorm=1)