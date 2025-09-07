import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(10, 8)
output = torch.fft.ifft(input)