import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 4, requires_grad=True)
output = torch.fft.fft(input, n=None, dim=(- 1), norm=None)