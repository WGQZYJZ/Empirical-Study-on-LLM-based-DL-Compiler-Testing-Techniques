import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, dtype=torch.float)
other = torch.randn(2, 3, dtype=torch.float)
torch.floor_divide(input, other)
torch.floor_divide(input, other, out=None)
torch.floor_divide(input, other, out=torch.empty(2, 3))