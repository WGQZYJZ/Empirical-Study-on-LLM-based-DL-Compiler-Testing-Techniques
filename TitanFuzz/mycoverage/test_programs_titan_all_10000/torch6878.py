import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 2, 2)
bn = torch.nn.BatchNorm2d(3)
output = bn(input)