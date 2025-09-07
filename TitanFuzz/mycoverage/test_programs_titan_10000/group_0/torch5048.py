import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(10)
other = torch.randn(10)
xlogy = torch.special.xlogy(input, other)