import torch
from torch import nn
from torch.autograd import Variable

input = torch.arange(0, 8).reshape(1, 2, 2, 2)
output = torch.fft.rfftn(input, s=None, dim=None, norm=None, out=None)