import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5, requires_grad=True)
output = torch.fft.irfft2(input)