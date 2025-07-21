import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1))
y = torch.rsqrt(x)
y = torch.rsqrt(x, out=x)