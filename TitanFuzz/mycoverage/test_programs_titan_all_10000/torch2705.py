import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 1)
y = torch.atleast_2d(x)