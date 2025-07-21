import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 4, 4)
output = torch.fft.fftshift(input, dim=None)