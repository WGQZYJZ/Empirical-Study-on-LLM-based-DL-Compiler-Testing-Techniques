import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3)
other = torch.randn(4, 3)
torch.cross(input, other)
input = torch.randn(4, 3)
torch.cumprod(input, dim=0)