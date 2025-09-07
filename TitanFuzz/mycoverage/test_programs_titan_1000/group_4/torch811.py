import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.atleast_1d(x)