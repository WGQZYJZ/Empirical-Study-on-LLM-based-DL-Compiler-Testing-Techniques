import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1)
a = torch.rand(1)
y = torch.special.gammainc(x, a)