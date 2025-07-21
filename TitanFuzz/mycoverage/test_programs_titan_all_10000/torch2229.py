import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, 3)
exponent = torch.tensor([1, 2, 3])
output = torch.float_power(input, exponent)