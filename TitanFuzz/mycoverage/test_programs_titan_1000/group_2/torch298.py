import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 4, 4)
output = torch.fft.ifft2(input)