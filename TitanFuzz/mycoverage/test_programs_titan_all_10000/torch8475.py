import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.rand(4, 4))
other = Variable(torch.rand(4, 4))
output = torch.special.gammaincc(input, other)