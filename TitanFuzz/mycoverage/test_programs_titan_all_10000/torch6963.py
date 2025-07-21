import torch
from torch import nn
from torch.autograd import Variable
input = (torch.rand(100, 1) * 100)
torch.histc(input, bins=100, min=0, max=0, out=None)