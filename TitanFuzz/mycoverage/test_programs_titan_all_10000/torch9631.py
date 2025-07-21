import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1000)
histc = torch.histc(input, bins=100, min=0, max=1)
histc = torch.histc(input, bins=100, min=0, max=1, out=torch.zeros(100))