import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5, 5)
output = torch.nn.AdaptiveAvgPool2d(3)(input)