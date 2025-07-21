import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 32, 32))
output = torch.nn.AdaptiveAvgPool2d(output_size=(4, 4))(input)