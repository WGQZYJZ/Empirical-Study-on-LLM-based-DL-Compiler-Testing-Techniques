import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 10)
y = torch.clamp(x, min=(- 0.5), max=0.5)
y = torch.clamp_max(x, max=0.5)
y = torch.clamp_min(x, min=(- 0.5))
y = torch.clamp_max_(x, max=0.5)
y = torch.clamp_min_(x, min=(- 0.5))