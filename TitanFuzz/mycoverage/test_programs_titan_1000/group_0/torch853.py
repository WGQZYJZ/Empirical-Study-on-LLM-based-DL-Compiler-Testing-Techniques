import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.AdaptiveMaxPool2d(2)(input)