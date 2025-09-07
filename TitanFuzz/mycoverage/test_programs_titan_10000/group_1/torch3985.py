import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(4, 4)
other = torch.randn(4, 4)
result = torch.less_equal(input, other)