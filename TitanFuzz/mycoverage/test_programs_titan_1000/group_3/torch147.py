import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 4)
other = torch.randn(1, 4)
output = torch.fmax(input, other)