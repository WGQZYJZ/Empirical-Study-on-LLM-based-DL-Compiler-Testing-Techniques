import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5)
avgpool = torch.nn.AdaptiveAvgPool1d(1)
output = avgpool(input)