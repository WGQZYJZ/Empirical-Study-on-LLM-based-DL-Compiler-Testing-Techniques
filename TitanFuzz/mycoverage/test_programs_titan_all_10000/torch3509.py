import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.fft.ifft(input, n=None, dim=(- 1), norm=None, out=None)