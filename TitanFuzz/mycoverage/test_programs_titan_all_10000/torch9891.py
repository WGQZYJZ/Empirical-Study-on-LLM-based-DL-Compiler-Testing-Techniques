import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
other = torch.randn(1, 3)
torch.logical_or(input, other)