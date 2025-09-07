import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4, 5)
output = torch.diff(input, n=1, dim=(- 1), prepend=None, append=None)