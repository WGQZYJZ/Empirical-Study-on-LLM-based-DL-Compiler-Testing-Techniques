import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 3)
y = torch.clip(x, min=(- 0.5), max=0.5)