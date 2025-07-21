import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(8, 8)
out = torch.fft.rfft(input)
input = torch.randn(8, 8)
out = torch.fft.irfft(input)