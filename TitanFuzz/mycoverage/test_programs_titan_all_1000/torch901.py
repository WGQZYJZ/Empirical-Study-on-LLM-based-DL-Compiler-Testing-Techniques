import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
y = torch.special.i1e(x)