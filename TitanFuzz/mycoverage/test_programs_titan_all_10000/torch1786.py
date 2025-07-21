import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
other = torch.randn(3, 4)
result = torch.less_equal(input, other)