import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4)
out = torch.special.i0(input)