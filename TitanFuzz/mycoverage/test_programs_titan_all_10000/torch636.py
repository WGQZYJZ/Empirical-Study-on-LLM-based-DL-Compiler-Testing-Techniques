import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1)
other = torch.randn(1)
output = torch.logaddexp2(input, other)