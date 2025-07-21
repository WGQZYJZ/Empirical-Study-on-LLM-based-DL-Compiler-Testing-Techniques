import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 4)
exponent = torch.rand(4, 4)
out = torch.float_power(input, exponent)