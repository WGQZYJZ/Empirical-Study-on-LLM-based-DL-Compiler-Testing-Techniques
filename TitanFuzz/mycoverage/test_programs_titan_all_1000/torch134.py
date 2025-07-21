import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
other = Variable(torch.randn(2, 3))
output = torch.igammac(input, other)