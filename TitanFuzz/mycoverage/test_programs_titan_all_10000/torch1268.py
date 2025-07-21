import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 4)
output = torch.fft.irfft(input, dim=(- 1))