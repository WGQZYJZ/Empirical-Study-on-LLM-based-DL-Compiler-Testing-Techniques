import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 4, 5)
output = torch.fft.fftshift(input)
output = torch.fft.fftshift(input, 2)