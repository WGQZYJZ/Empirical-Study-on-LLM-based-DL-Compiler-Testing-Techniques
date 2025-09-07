import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(10, 10)
exponent = torch.randn(10, 10)
output = torch.float_power(input, exponent)
input = torch.randn(10, 10)
exponent = torch.randn(10, 10)
output = torch.pow(input, exponent)
input = torch.randn(10, 10)
exponent = torch.randn(10, 10)
output = torch.pow(input, exponent)
input = torch.randn