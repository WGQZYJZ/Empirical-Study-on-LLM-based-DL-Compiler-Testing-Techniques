import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1)
x = Variable(x, requires_grad=True)
y = torch.special.log1p(x)
y.backward()