import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4, 5, 6)
y = torch.fft.fftn(x, norm=None)