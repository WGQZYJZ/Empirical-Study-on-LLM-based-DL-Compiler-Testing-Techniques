import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 5, 5)
x = Variable(x)
y = torch.fft.fftshift(x)