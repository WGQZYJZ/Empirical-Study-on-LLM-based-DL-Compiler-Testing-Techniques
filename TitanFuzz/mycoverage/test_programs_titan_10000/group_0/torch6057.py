import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(5, 5)
other = torch.randn(5)
torch.inner(input, other)
out = torch.empty(5)
torch.inner(input, other, out=out)