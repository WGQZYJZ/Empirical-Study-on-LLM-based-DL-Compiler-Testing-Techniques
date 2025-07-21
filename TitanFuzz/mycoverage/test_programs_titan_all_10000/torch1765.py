import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 2)
exponent = torch.randn(2, 2)
output = torch.float_power(input, exponent)