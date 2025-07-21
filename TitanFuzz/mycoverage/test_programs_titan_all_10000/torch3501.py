import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 1, 1, requires_grad=True)
output = torch.fix(input)
input = torch.randn(1, 1, 1, 1, requires_grad=True)
output = torch.floor(input)
input = torch.randn(1, 1, 1, 1, requires_grad=True)
other = torch.randn(1, 1, 1, 1, requires_grad=True)
output = torch.floor_divide(input, other)