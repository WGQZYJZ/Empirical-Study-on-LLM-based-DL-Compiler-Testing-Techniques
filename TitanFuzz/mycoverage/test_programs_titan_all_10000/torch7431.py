import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(16, 16)
output = torch.fft.fftshift(input, dim=None)