import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3))
output = torch.abs(input)