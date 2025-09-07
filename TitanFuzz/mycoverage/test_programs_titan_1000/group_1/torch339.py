import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3))
conv2d = torch.nn.functional.conv2d(input, Variable(torch.ones(1, 1, 2, 2)), None, 1, 1)