import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 4, 5)
output = torch.fft.ifft(input, norm=None)