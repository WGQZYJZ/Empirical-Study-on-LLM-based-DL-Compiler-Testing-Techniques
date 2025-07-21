import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4, 5)
other = torch.randn(1, 2, 3, 4, 5)
output = torch.logaddexp2(input, other)
input = torch.randn(1, 2, 3, 4, 5)
other = torch.randn(1, 2, 3, 4, 5)
output = torch.logical_and(input, other)
input = torch.randn(1, 2, 3, 4, 5)
output = torch.log