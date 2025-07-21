import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(100, 100, 100, 100)
torch.fft.irfft2(input)