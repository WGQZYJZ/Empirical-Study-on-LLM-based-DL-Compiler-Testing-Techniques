import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
exponent = torch.randn(3, 3)
result = torch.float_power(input, exponent)