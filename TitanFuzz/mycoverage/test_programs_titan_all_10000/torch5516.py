import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.greater_equal(input, other)