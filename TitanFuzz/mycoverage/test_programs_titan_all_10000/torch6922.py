import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(8, 4)
torch.vsplit(input, 4)