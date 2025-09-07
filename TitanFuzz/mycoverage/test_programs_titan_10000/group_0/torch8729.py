import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 1)
y = torch.atleast_2d(x)
z = torch.atleast_2d(x, x, x)