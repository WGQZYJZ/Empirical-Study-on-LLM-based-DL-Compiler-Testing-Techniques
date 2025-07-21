import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
input[(1, 2)] = float('nan')
input[(2, 3)] = float('nan')
sum_ = torch.nansum(input, dim=1)