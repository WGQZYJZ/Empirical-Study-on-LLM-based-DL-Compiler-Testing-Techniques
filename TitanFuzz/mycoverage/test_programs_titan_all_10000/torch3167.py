import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4)
torch.fft.irfftn(input, s=None, dim=None, norm=None, out=None)