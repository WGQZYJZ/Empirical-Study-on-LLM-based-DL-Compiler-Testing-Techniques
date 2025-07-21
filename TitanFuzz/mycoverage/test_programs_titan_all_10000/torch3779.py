import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4)
y = torch.randn(4).mul(2).floor()
z = torch.ldexp(x, y)