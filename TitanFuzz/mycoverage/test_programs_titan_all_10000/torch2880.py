import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 1)
other = torch.randn(3, 1)
minimum = torch.minimum(input, other)