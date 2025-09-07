import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.gt(input, other)
input = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.ge(input, other)