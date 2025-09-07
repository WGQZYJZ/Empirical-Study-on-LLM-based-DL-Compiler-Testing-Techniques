import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 4, 5)
output = torch.fft.fft(input)
input = torch.randn(1, 4, 5)
output = torch.fft.ifft(input)