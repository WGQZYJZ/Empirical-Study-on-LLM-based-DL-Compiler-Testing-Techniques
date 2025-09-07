import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 1)
other = torch.rand(1, 1)
output = torch.special.gammainc(input, other)