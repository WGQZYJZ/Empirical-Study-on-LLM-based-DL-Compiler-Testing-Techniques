import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3, 3)
y = torch.fft.fftn(x, s=None, dim=None, norm=None)