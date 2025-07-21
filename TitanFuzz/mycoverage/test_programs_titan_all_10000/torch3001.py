import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 4)
output = torch.fft.rfft(input, n=None, dim=(- 1), norm=None, out=None)