import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 2, 2)
torch.fft.irfft2(input)