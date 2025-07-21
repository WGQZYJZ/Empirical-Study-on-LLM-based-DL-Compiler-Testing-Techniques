import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(7, 4)
output = torch.split(input, 2, dim=0)