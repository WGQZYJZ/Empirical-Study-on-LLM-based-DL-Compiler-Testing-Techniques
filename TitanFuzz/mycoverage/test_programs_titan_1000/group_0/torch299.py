import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3)
y = torch.positive(x)
z = torch.clamp(x, min=(- 0.5), max=0.5)