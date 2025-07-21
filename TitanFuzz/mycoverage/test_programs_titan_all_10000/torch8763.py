import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.special.gammaincc(input, other)
torch.special.gammaincc(input, other, out=None)