import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 10)
output = torch.nn.AdaptiveAvgPool1d(3)(input)