import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(1, requires_grad=True)
b = torch.log1p(a)
c = (torch.exp(a) - 1)
d = (torch.exp(a) - 1).mean()
e = torch.log1p(a).mean()