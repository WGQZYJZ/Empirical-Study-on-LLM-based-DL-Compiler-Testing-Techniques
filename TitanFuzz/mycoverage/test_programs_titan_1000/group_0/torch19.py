import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 4, 8)
y = torch.fft.rfft(x)