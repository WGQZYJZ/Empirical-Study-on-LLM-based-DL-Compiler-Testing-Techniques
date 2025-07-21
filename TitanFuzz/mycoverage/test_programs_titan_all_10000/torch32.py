import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 32, 32))
output = torch.nn.AdaptiveMaxPool2d((4, 4))(input)