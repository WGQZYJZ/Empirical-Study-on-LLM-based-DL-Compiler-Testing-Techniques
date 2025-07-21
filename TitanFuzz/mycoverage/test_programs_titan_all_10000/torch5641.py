import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
a = torch.randn(4, 4)
y = torch.special.gammainc(x, a)