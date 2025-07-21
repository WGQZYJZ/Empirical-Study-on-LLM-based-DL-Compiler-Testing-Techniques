import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.AdaptiveMaxPool3d(3)(input)
input = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.AdaptiveAvgPool3d(3)(input)