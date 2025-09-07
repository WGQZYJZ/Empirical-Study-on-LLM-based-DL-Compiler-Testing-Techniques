import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10)
values = torch.randn(10)
out = torch.heaviside(input, values)