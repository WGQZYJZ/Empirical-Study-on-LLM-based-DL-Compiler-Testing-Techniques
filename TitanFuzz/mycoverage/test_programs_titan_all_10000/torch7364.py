import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(100)
output = torch.histc(input, bins=100, min=0, max=0)