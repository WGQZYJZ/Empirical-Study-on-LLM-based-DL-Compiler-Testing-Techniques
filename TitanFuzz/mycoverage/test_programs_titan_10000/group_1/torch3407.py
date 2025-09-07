import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(4, 4)
other = torch.rand(4, 4)
out = torch.greater(input, other)