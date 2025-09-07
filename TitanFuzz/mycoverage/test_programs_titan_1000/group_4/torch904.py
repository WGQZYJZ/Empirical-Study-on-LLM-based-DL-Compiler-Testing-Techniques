import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1000)
hist = torch.histc(input, bins=100, min=0, max=0)