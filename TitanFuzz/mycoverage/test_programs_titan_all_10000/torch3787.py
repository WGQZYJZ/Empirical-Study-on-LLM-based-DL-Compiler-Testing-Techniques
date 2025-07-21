import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, 2, 2)
output = torch.fft.irfft2(input)