import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 2, 2)
output = torch.fft.ifft(input)