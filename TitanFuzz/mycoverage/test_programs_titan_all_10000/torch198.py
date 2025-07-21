import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 10)
other = torch.randn(10, 10)
output = torch.sub(input, other)