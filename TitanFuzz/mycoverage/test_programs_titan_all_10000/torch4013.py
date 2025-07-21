import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3)
output = torch.fft.fft2(input)