import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
input[(0, 0)] = float('nan')
input[(1, 2)] = float('nan')
quantile = torch.nanquantile(input, 0.5, dim=0, keepdim=False)