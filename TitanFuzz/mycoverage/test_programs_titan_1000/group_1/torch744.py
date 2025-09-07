import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, requires_grad=True)
other = torch.tensor([1.0, 2.0, 3.0])
output = torch.le(input, other)