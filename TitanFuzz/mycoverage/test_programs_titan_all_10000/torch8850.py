import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1000)
torch.histc(x, bins=100, min=0, max=0, out=None)