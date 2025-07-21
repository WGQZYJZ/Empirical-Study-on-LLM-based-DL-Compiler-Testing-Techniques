import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10)
y = torch.clamp(x, min=(- 0.5), max=0.5)