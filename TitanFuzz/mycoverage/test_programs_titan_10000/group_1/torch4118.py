import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(4, 8, 16)
output = torch.fft.ihfft(input)