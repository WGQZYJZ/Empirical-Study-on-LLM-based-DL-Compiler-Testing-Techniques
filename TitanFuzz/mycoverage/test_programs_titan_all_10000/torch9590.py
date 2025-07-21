import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
output = torch.fft.rfft2(input)
input = torch.randn(2, 3, 4, 5)
output = torch.fft.irfft2(input)