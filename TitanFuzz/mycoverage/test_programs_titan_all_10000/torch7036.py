import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 10)
fft_x = torch.fft.fftn(x)