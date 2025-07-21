import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
out = torch.igamma(input, other)