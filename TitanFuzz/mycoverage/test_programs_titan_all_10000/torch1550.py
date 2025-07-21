import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
output = torch.fft.rfftn(input, s=None, dim=None, norm=None, out=None)