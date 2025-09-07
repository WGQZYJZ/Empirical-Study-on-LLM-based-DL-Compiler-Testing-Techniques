import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 4)
torch.fft.rfft(input, n=None, dim=(- 1), norm=None, out=None)