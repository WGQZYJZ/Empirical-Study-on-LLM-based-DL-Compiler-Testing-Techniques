import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 10, 2)
output = torch.fft.rfft(input, n=None, dim=(- 1), norm=None, out=None)