import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5))
output = torch.nn.AdaptiveAvgPool1d(4)(input)