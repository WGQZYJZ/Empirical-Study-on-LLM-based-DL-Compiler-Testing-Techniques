import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, 3)
input[(0, 0, 0)] = float('nan')
input[(1, 1, 1)] = float('nan')
input[(2, 2, 2)] = float('nan')
result = torch.nansum(input, dim=2)