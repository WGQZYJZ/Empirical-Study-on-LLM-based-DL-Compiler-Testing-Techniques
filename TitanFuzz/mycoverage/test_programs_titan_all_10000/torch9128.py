import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
mean = torch.mean(input)
mean = torch.mean(input, dim=0)