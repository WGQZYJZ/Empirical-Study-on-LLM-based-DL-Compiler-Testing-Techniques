import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
output = torch.fft.irfft(input_data, n=None, dim=(- 1), norm=None, out=None)