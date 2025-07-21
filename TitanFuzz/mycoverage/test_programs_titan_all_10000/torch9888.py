import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4)
other = torch.randn(4)
result = torch.copysign(input, other)