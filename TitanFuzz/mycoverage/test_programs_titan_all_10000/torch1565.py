import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(16, 8)
output = torch.fft.rfft2(input)