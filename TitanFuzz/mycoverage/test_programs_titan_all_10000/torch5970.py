import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
output = torch.nn.Hardsigmoid(inplace=False)(input)