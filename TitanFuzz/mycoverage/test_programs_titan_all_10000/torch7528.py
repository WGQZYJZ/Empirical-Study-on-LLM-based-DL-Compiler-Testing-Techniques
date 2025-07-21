import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(4, 4))
other = Variable(torch.randn(4, 4))
output = torch.special.gammainc(input, other)