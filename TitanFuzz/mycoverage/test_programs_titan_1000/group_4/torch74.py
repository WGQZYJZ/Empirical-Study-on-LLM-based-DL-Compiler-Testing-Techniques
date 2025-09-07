import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 5, 6, 7, 8)
output = torch.fft.fftn(input)