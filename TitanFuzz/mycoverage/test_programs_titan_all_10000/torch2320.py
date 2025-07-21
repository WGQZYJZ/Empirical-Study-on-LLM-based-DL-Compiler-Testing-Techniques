import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
shifts = 1
dims = 0
output = torch.roll(input, shifts, dims)