import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
input = input.abs()
output = torch.mvlgamma(input, p=1)