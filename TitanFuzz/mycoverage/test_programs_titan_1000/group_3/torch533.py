import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4)
b = torch.randn(4)
c = torch.fmax(a, b)
d = torch.fmax(a, b, out=c)