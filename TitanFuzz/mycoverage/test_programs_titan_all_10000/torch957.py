import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 3, 3)
b = torch.randn(3, 3, 3)
c = torch.fft.ifftn(a, s=None, dim=None, norm=None, out=None)