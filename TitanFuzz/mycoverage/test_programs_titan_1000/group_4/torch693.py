import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.diagflat(input)
output = torch.diagflat(input, offset=1)
output = torch.diagflat(input, offset=(- 1))