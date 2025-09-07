import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 10)
other = torch.randn(1, 10)
torch.logaddexp(input, other)