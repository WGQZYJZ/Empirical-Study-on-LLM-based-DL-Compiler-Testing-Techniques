import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 2, 2))
torch.fft.ifftn(input)
input = Variable(torch.randn(1, 1, 2, 2))