import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(1, 1)
b = torch.randn(2, 1)
c = torch.randn(3, 1)
torch.atleast_1d(a, b, c)