import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 3, 4)
y = torch.randn(2, 3, 4)
z = torch.atleast_1d(x, y)