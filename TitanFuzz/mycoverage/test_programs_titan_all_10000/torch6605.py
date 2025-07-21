import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 5)
torch.vsplit(input, [3, 6])