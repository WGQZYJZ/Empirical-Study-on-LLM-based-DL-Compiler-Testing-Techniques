import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input)