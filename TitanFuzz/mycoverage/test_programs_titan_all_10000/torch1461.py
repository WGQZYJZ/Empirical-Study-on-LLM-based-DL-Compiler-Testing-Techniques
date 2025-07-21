import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 2, 2)
output = torch.fft.irfft2(input)