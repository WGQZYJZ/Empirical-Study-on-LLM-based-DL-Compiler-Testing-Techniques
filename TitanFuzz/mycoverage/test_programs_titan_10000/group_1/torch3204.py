import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(5)
other = torch.randn(5)
result = torch.minimum(input, other)