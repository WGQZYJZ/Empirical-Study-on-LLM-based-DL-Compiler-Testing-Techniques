import torch
from torch import nn
from torch.autograd import Variable
N = 16
x = torch.randn(N, N, N)
y = torch.fft.irfftn(x)