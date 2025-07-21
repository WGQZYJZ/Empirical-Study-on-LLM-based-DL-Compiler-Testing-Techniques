import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 10)
other = torch.randn(10)
output = torch.inner(input, other)