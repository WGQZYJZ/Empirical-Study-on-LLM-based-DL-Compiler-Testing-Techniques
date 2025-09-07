import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
input[(0, 1)] = float('nan')
input[(1, 2)] = float('nan')
output = torch.nanmean(input, dim=0)