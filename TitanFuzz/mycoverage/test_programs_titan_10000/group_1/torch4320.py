import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(5)
y = torch.randn(5)
z = torch.logaddexp(x, y)