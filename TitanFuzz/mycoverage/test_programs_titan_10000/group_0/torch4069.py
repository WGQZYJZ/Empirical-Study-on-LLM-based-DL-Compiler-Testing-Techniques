import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 1)
x = torch.randn(1)
x = torch.randn(1)
x = torch.atleast_2d(x)