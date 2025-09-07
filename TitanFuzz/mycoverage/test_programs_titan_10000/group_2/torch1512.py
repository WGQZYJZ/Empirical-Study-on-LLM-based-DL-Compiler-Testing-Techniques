import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
other = torch.randn(3, 3)
output = torch.not_equal(input, other)