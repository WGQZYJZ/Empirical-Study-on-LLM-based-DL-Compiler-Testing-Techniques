import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
c = (a + b)
d = c.sum()
torch._assert(d.requires_grad, 'd must require grad')